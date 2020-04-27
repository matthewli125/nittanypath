from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Max, Min, Avg
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from ntnyPth.models import *
from ntnyPth.forms import *

from datetime import datetime

# Create your views here.

homework_weight = 0.7
exam_weight = 0.3
grades = ["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A"]

@login_required
def change_password(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password successfully changed.")
            return redirect(user_home)
        else:
            messages.error(request, "Password change failed.")

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'registration/password_change_form.html', {"form": form})


def get_user(username):
    user = 0
    user_type = 0

    try: user, user_type = Professor.objects.get(email=username), "professor"
    except Professor.DoesNotExist: pass

    try: user, user_type = Student.objects.get(email=username), "student"
    except Student.DoesNotExist: pass

    return user, user_type


def get_hwgrade(email, cid):
    return Homework_grade.objects.filter(course_id_id=cid, student_email_id=email).aggregate(Avg('grade'))['grade__avg']


def get_examgrade(email, cid):
    return Exam_grade.objects.filter(course_id_id=cid, student_email_id=email).aggregate(Avg('grades'))['grades__avg']


def get_grades(email, cid):
    hw_grade = get_hwgrade(email, cid)
    exam_grade = get_examgrade(email, cid)

    if not hw_grade:
        hw_grade = 0
    if not exam_grade:
        exam_grade = 0

    return round(homework_weight * hw_grade + exam_weight * exam_grade, 2)


def calculate_grade(percent):
    x = int(percent)
    return grades[int((x // 60) * (x // 3.5 - 16) * (100 // (x + 1)) + (x % 10 == 0)*(x < 100) - (x == 98) - (x == 99) + (x > 100) * 11)]


@login_required
def user_home(request):

    email = request.user.username
    user, user_type = get_user(email)

    if user == 0 or user_type == 0:
        return render(request, "errors/error.html")

    if user_type == "student":
        enrolled = Enroll.objects.filter(student_email_id=user.email)

        teaching_team_id = None
        ta_courses = None

        try: teaching_team_id = TA_teaching_team.objects.get(student_email_id=user.email).teaching_team_id
        except TA_teaching_team.DoesNotExist: pass

        if teaching_team_id:
            tas = [(i.course_id_id, i.sec_no) for i in Section.objects.filter(teaching_team_id=teaching_team_id)]
            ta_courses = [[Course.objects.get(course_id=i[0]), get_image(i[0]), i[1]] for i in tas]

        data = {"classes": [[Course.objects.get(course_id=i.course_id_id), get_image(i.course_id_id)] for i in enrolled],
                "name": user.name, "major": user.major, "gender": user.gender, "age": user.age, "street": user.street,
                "city": user.zipcode.city, "state": user.zipcode.state, "zip": user.zipcode.zipcode, "ta_courses": ta_courses}
        return render(request, "homepages/student_home.html", data)
    else:
        teaching_team_id = Prof_teaching_team.objects.get(prof_email_id=user.email).teaching_team_id
        courses = [(i.course_id_id, i.sec_no) for i in Section.objects.filter(teaching_team_id=teaching_team_id)]
        data = {"classes": [[Course.objects.get(course_id=i[0]), get_image(i[0]), i[1]] for i in courses], "name": user.name}
        return render(request, "homepages/prof_home.html", data)



def get_image(course_id):
    src = 'img/classes/{}.jpg'.format("".join([i for i in list(course_id) if not i.isdigit()]))
    return src


@login_required
def prof_class_info(request, course_id, name, sec_no):

    email = request.user.username
    course = Course.objects.get(course_id=course_id)
    section = Section.objects.get(sec_no=sec_no, course_id_id=course_id)

    c_dept = "".join(i for i in list(course_id) if not i.isdigit())
    c_num = "".join(i for i in list(course_id) if i.isdigit())

    hws = Homework.objects.filter(course_id_id=course_id, sec_no=sec_no)
    exams = Exam.objects.filter(course_id_id=course_id, sec_no=sec_no)

    request.session["course_id"] = course_id
    request.session["name"] = name
    request.session["sec_no"] = sec_no

    data = {"hws": hws, "exams": exams, "c_name": course.course_name,
            "description": course.course_description, "c_dept": c_dept,
            "c_num": c_num, "sec_no": sec_no, "name": name}
    return render(request, "classes_info/prof_class_page.html", data)


@login_required
def student_class_info(request, course_id, name):
    email = request.user.username
    course = Course.objects.get(course_id=course_id)
    en = Enroll.objects.get(student_email_id=email, course_id_id=course_id)
    section = Section.objects.get(sec_no=en.sec_no, course_id_id=course_id)

    prof = Prof_teaching_team.objects.get(teaching_team_id=section.teaching_team_id).prof_email

    c_dept = "".join(i for i in list(course_id) if not i.isdigit())
    c_num = "".join(i for i in list(course_id) if i.isdigit())

    request.session["course_id"] = course_id
    request.session["sec_no"] = en.sec_no

    hws = Homework.objects.filter(course_id_id=course_id, sec_no=en.sec_no)
    hw_grades = [(i.hw_no, i.hw_details, get_hw_grade(i, email)) for i in hws]

    raw_grade_new = get_grades(email, course_id)
    letter_grade_new = calculate_grade(raw_grade_new)

    raw_grade = en.raw_grade
    letter_grade = en.grade

    if raw_grade_new != raw_grade:
        raw_grade = raw_grade_new
        letter_grade = letter_grade_new
        en.raw_grade = raw_grade_new
        en.grade = letter_grade_new
        en.save()

    exams = Exam.objects.filter(course_id_id=course_id, sec_no=en.sec_no)
    exam_grades = [(i.exam_no, i.exam_details, get_exam_grade(i, email)) for i in exams]

    data = {"hws": hw_grades, "c_dept": c_dept, "c_num": c_num, "course_id": course_id,
            "c_name": course.course_name, "deadline": course.late_drop_deadline, "section": en.sec_no, "name": name,
            "description": course.course_description, "prof_name": prof.name, "prof_email": prof.email,
            "prof_office": prof.office_address, "exams": exam_grades, "letter_grade": letter_grade, "raw_grade": raw_grade}

    return render(request, "classes_info/student_class_page.html", data)


def get_hw_grade(hw, email):
    grade = "Not yet graded"
    try: grade = Homework_grade.objects.get(course_id_id=hw.course_id_id, sec_no=hw.sec_no, student_email_id=email, hw_no=hw.hw_no).grade
    except Homework_grade.DoesNotExist: pass

    return grade


def get_exam_grade(exam, email):
    grade = "Not yet graded"
    try: grade = Exam_grade.objects.get(course_id_id=exam.course_id_id, sec_no=exam.sec_no, student_email_id=email, exam_no=exam.exam_no).grades
    except Exam_grade.DoesNotExist: pass

    return grade


@login_required
def drop_class(request, course_id):

    email = request.user.username


    drop_deadline = Course.objects.get(course_id=course_id).late_drop_deadline
    today = datetime.today()

    if today.date() < drop_deadline:
        Enroll.objects.filter(student_email_id=email, course_id_id=course_id).delete()
        Exam_grade.objects.filter(student_email_id=email, course_id_id=course_id).delete()
        Homework_grade.objects.filter(student_email_id=email, course_id_id=course_id).delete()
        Post.objects.filter(student_email_id=email, course_id_id=course_id).delete()
        Comment.objects.filter(student_email_id=email, course_id_id=course_id).delete()
        messages.success(request, "Class successfully droppped.")

    return redirect(user_home)


@login_required
def add_assignment(request, atype, anum, adet):

    course_id = request.session["course_id"]
    name = request.session["name"]
    sec_no = request.session["sec_no"]

    if atype == "hw" and not Homework.objects.filter(sec_no=sec_no, hw_no=anum, course_id_id=course_id):
        Homework.objects.create(sec_no=sec_no, hw_no=anum, hw_details=adet, course_id_id=course_id)

    if atype == "exam" and not Exam.objects.filter(sec_no=sec_no, exam_no=anum, course_id_id=course_id):
        Exam.objects.create(sec_no=sec_no, exam_no=anum, exam_details=adet, course_id_id=course_id)

    return prof_class_info(request, course_id, name, sec_no)


@login_required
def delete_assignment(request, atype, anum):

    course_id = request.session["course_id"]
    name = request.session["name"]
    sec_no = request.session["sec_no"]

    if atype == "hw" and Homework.objects.filter(sec_no=sec_no, hw_no=anum, course_id_id=course_id):
        Homework.objects.filter(sec_no=sec_no, hw_no=anum, course_id_id=course_id).delete()
        Homework_grade.objects.filter(sec_no=sec_no, hw_no=anum, course_id_id=course_id).delete()

    if atype == "exam" and Exam.objects.filter(sec_no=sec_no, exam_no=anum, course_id_id=course_id):
        Exam.objects.filter(sec_no=sec_no, exam_no=anum, course_id_id=course_id).delete()
        Exam_grade.objects.filter(sec_no=sec_no, exam_no=anum, course_id_id=course_id).delete()

    return prof_class_info(request, course_id, name, sec_no)


@login_required
def assignment_details(request, atype, anum):

    course_id = request.session["course_id"]
    sec_no = request.session["sec_no"]

    request.session["atype"] = atype
    request.session["anum"] = anum

    student_emails = Enroll.objects.filter(course_id_id=course_id, sec_no=sec_no)
    students = [Student.objects.get(email=i.student_email_id) for i in student_emails]

    c_dept = "".join(i for i in list(course_id) if not i.isdigit())
    c_num = "".join(i for i in list(course_id) if i.isdigit())

    user, user_type = get_user(request.user.username)

    grade = None
    avg_grade = "NA"
    min_grade = "NA"
    max_grade = "NA"

    if atype == "exam":
        exam = Exam.objects.get(course_id_id=course_id, sec_no=sec_no, exam_no=anum)
        grades = [(student, get_exam_grade(exam, student.email)) for student in students]

        if user_type == "student":
            grade = get_exam_grade(exam, request.user.username)

        aname = "Exam {}".format(anum)
        atype = "exam"
        adet = exam.exam_details

        all_grades = Exam_grade.objects.filter(course_id_id=course_id, sec_no=sec_no, exam_no=anum)
        if all_grades:
            avg_grade = all_grades.aggregate(Avg('grades'))['grades__avg']
            min_grade = all_grades.aggregate(Min('grades'))['grades__min']
            max_grade = all_grades.aggregate(Max('grades'))['grades__max']

    else:
        hw = Homework.objects.get(course_id_id=course_id, sec_no=sec_no, hw_no=anum)
        grades = [(student, get_hw_grade(hw, student.email)) for student in students]

        if user_type == "student":
            grade = get_hw_grade(hw, request.user.username)

        aname = "Homework {}".format(anum)
        atype = "hw"
        adet = hw.hw_details

        all_grades = Homework_grade.objects.filter(course_id_id=course_id, sec_no=sec_no, hw_no=anum)
        if all_grades:
            avg_grade = round(all_grades.aggregate(Avg('grade'))['grade__avg'], 2)
            min_grade = all_grades.aggregate(Min('grade'))['grade__min']
            max_grade = all_grades.aggregate(Max('grade'))['grade__max']

    if user_type == "professor":
        graded_students = [i for i in grades if i[1] != "Not yet graded"]
        ungraded_students = [i for i in grades if i[1] == "Not yet graded"]
        grade = None
    else:
        graded_students = []
        ungraded_students = []


    data = {"sec_no": sec_no, "grades": grades, "graded_students": graded_students,
            "ungraded_students":ungraded_students, "aname": aname, "c_dept": c_dept,
            "atype": atype, "anum": anum, "adet": adet, "c_num": c_num, "avg": avg_grade,
            "min": min_grade, "max": max_grade, "user_type": user_type, "grade": grade}

    return render(request, "classes_info/assignment_details.html", data)


@login_required
def create_grade(request, student_email, grade):

    course_id = request.session["course_id"]
    sec_no = request.session["sec_no"]
    atype = request.session["atype"]
    anum = request.session["anum"]

    if atype == "exam":
        exist = Exam_grade.objects.filter(student_email_id=student_email, course_id_id=course_id, sec_no=sec_no, exam_no=anum)

        if not exist:
            Exam_grade.objects.create(student_email_id=student_email, course_id_id=course_id, sec_no=sec_no, exam_no=anum, grades=grade)
        else:
            new_grade = list(exist)[0]
            new_grade.grades = grade
            new_grade.save()

    else:
        exist = Homework_grade.objects.filter(student_email_id=student_email, course_id_id=course_id, sec_no=sec_no, hw_no=anum)

        if not exist:
            student = Student.objects.get(email=student_email)
            Homework_grade.objects.create(student_email_id=student.email, course_id_id=course_id, sec_no=sec_no, hw_no=anum, grade=grade)
        else:
            new_grade = list(exist)[0]
            new_grade.grade = grade
            new_grade.save()

    enrollment = Enroll.objects.get(course_id_id=course_id, student_email_id=student_email)
    enrollment.raw_grade = get_grades(student_email, course_id)
    enrollment.grade = calculate_grade(enrollment.raw_grade)
    enrollment.save()

    return assignment_details(request, atype, anum)


@login_required
def posts(request, email):
    course_id = request.session["course_id"]

    c_dept = "".join(i for i in list(course_id) if not i.isdigit())
    c_num = "".join(i for i in list(course_id) if i.isdigit())
    c_name = Course.objects.get(course_id=course_id).course_name

    if email == "all":
        query = Post.objects.filter(course_id_id=course_id)
    else:
        query = Post.objects.filter(course_id_id=course_id, student_email=email)

    all_posts = [(get_user(i.student_email), i, (i.post_info[:30]+"..." if len(i.post_info) > 30 else i.post_info),
                                                (i.post_info[:150]+". . ." if len(i.post_info) > 150 else i.post_info)) for i in query]

    data = {"c_dept": c_dept, "c_num": c_num, "c_name": c_name, "user_email": request.user.username, "posts": sorted(all_posts, reverse=True, key=lambda x: x[1].post_no)}

    return render(request, "forum/forum.html", data)


@login_required
def post_detail(request, pk):
    course_id = request.session["course_id"]
    c_name = Course.objects.get(course_id=course_id).course_name
    c_dept = "".join(i for i in list(course_id) if not i.isdigit())
    c_num = "".join(i for i in list(course_id) if i.isdigit())

    post = Post.objects.get(pk=pk)
    poster = get_user(post.student_email)
    request.session["post_no"] = post.post_no
    request.session["post_pk"] = pk
    comments = [[get_user(i.student_email), i] for i in Comment.objects.filter(course_id_id=post.course_id, post_no = post.post_no)]

    data = {"poster": poster, "c_dept": c_dept, "c_num": c_num, "c_name": c_name, "post": post, "comments": sorted(comments, reverse=True, key=lambda x: x[1].comment_no)}

    return render(request, "forum/forum_post.html", data)


@login_required
def new_post(request):
    course_id = request.session["course_id"]
    course = Course.objects.get(course_id=course_id)
    c_name = course.course_name
    c_dept = "".join(i for i in list(course_id) if not i.isdigit())
    c_num = "".join(i for i in list(course_id) if i.isdigit())

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.student_email = request.user.username
            post.course_id = course

            posts_all = Post.objects.filter(course_id_id=course_id, post_no__gt=0)

            if posts_all:
                post.post_no = posts_all.aggregate(Max('post_no'))['post_no__max'] + 1
            else:
                post.post_no = 1

            post.save()
            return redirect('posts', email='all')

    return render(request, "forum/new_post.html", {"c_dept": c_dept, "c_num": c_num, "c_name": c_name})


@login_required
def new_comment(request):
    course_id = request.session["course_id"]

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.student_email = request.user.username
            comment.course_id = Course.objects.get(course_id=course_id)
            comment.post_no = request.session["post_no"]

            comments_all = Comment.objects.filter(course_id_id=course_id, post_no=comment.post_no)

            if comments_all:
                comment.comment_no = comments_all.aggregate(Max('comment_no'))['comment_no__max'] + 1
            else:
                comment.comment_no = 1

            comment.save()

            return redirect('post_detail', pk=request.session["post_pk"])

    return redirect('post_detail', pk=request.session["post_pk"])


@login_required
def announcements(request):
    course_id = request.session["course_id"]
    sec_no = request.session["sec_no"]

    c_dept = "".join(i for i in list(course_id) if not i.isdigit())
    c_num = "".join(i for i in list(course_id) if i.isdigit())
    c_name = Course.objects.get(course_id=course_id).course_name

    user = get_user(request.user.username)

    query = Comment.objects.filter(course_id_id=course_id, post_no=-int(sec_no))
    all_anns = [(get_user(i.student_email), i, (i.comment_info[:30] + "..." if len(i.comment_info) > 30 else i.comment_info)) for i in query]

    data = {"c_dept": c_dept, "c_num": c_num, "c_name": c_name, "sec_no": sec_no, "user_type": user[1], "announcements": all_anns}

    return render(request, "announcements/announcement_page.html", data)


@login_required
def announcement_details(request, pk):
    course_id = request.session["course_id"]
    c_name = Course.objects.get(course_id=course_id).course_name
    c_dept = "".join(i for i in list(course_id) if not i.isdigit())
    c_num = "".join(i for i in list(course_id) if i.isdigit())
    sec_no = request.session["sec_no"]

    announcement = Comment.objects.get(pk=pk)
    poster = get_user(announcement.student_email)

    data = {"c_dept": c_dept, "c_num": c_num, "c_name": c_name, "sec_no": sec_no, "poster": poster, "announcement": announcement}

    return render(request, "announcements/announcement_details.html", data)


@login_required
def new_announcement(request):
    course_id = request.session["course_id"]
    sec_no = request.session["sec_no"]

    c_dept = "".join(i for i in list(course_id) if not i.isdigit())
    c_num = "".join(i for i in list(course_id) if i.isdigit())
    c_name = Course.objects.get(course_id=course_id).course_name

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.student_email = request.user.username
            comment.course_id = Course.objects.get(course_id=course_id)
            comment.post_no = -int(sec_no)

            comments_all = Comment.objects.filter(course_id_id=course_id, post_no=comment.post_no)

            if comments_all:
                comment.comment_no = comments_all.aggregate(Min('comment_no'))['comment_no__min'] - 1
            else:
                comment.comment_no = -1

            comment.save()

            return render(request, "announcements/announcement_details.html")

    data = {"c_dept": c_dept, "c_num": c_num, "c_name": c_name, "sec_no": sec_no}

    return render(request, "announcements/new_announcement.html", data)





