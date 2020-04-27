from django.conf import settings
import projectPhase2New.settings
from tqdm import tqdm

settings.configure(INSTALLED_APPS = projectPhase2New.settings.INSTALLED_APPS, DATABASES = projectPhase2New.settings.DATABASES)

import django
django.setup()

from ntnyPth.models import Enroll, Student, Homework_grade, Exam_grade
from django.db.models import Avg
from tqdm import tqdm

homework_weight = 0.7
exam_weight = 0.3
grades = ["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A"]


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


for i in tqdm(Enroll.objects.all()):
    i.raw_grade = get_grades(i.student_email_id, i.course_id_id)
    i.grade = calculate_grade(i.raw_grade)
    i.save()


