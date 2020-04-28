from django.db import models

# Create your models here.


class Student(models.Model):
    email = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    major = models.CharField(max_length=10)
    street = models.CharField(max_length=200)
    zipcode = models.ForeignKey('Zipcode', on_delete=models.DO_NOTHING)


class Zipcode(models.Model):
    zipcode = models.CharField(max_length=5, primary_key=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)


class Professor(models.Model):
    email = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    office_address = models.CharField(max_length=200)
    department = models.CharField(max_length=10)
    title = models.CharField(max_length=20)


class Department(models.Model):
    dept_id = models.CharField(max_length=10, primary_key=True)
    dept_name = models.CharField(max_length=100)
    dept_head = models.CharField(max_length=20)


class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=200)
    late_drop_deadline = models.DateField()


class Section(models.Model):
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    sec_no = models.PositiveIntegerField()
    limit = models.IntegerField()
    teaching_team_id = models.IntegerField()

    class Meta:
        unique_together = [['course_id', 'sec_no']]


class Enroll(models.Model):
    student_email = models.ForeignKey('Student', on_delete=models.CASCADE)
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    sec_no = models.PositiveIntegerField()
    grade = models.CharField(max_length=2)
    raw_grade = models.FloatField()

    class Meta:
        unique_together = [['student_email', 'course_id', 'sec_no']]


class Prof_teaching_team(models.Model):
    prof_email = models.ForeignKey('Professor', on_delete=models.CASCADE)
    teaching_team_id = models.IntegerField()

    class Meta:
        unique_together = [['prof_email', 'teaching_team_id']]


class TA_teaching_team(models.Model):
    student_email = models.ForeignKey('Student', on_delete=models.CASCADE)
    teaching_team_id = models.IntegerField()

    class Meta:
        unique_together = [['student_email', 'teaching_team_id']]


class Homework(models.Model):
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    sec_no = models.PositiveIntegerField()
    hw_no = models.PositiveIntegerField()
    hw_details = models.CharField(max_length=200)

    class Meta:
        unique_together = [['course_id', 'sec_no', 'hw_no']]


class Homework_grade(models.Model):
    student_email = models.ForeignKey('Student', on_delete=models.CASCADE)
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    sec_no = models.PositiveIntegerField()
    hw_no = models.PositiveIntegerField()
    grade = models.FloatField()

    class Meta:
        unique_together = [['student_email', 'course_id', 'sec_no', 'hw_no']]


class Exam(models.Model):
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    sec_no = models.PositiveIntegerField()
    exam_no = models.PositiveIntegerField()
    exam_details = models.CharField(max_length=200)

    class Meta:
        unique_together = [['course_id', 'sec_no', 'exam_no']]


class Exam_grade(models.Model):
    student_email = models.ForeignKey('Student', on_delete=models.CASCADE)
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    sec_no = models.PositiveIntegerField()
    exam_no = models.PositiveIntegerField()
    grades = models.FloatField()

    class Meta:
        unique_together = [['student_email', 'course_id', 'sec_no', 'exam_no']]


class Post(models.Model):
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    post_no = models.PositiveIntegerField()
    student_email = models.CharField(max_length=20)
    post_info = models.CharField(max_length=1000)

    class Meta:
        unique_together = [['course_id', 'post_no']]


class Comment(models.Model):
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    post_no = models.IntegerField()
    comment_no = models.IntegerField()
    student_email = models.CharField(max_length=20)
    comment_info = models.CharField(max_length=1000)

    class Meta:
        unique_together = [['course_id', 'post_no', 'comment_no']]
