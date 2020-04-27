from django.contrib import admin
from .models import *
# Register your models here.

from django.conf.locale.es import formats as es_formats

es_formats.DATETIME_FORMAT = "d M Y H:i:s"

admin.site.register(Student)
admin.site.register(Zipcode)
admin.site.register(Professor)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Enroll)
admin.site.register(Prof_teaching_team)
admin.site.register(TA_teaching_team)
admin.site.register(Homework)
admin.site.register(Homework_grade)
admin.site.register(Exam)
admin.site.register(Exam_grade)
admin.site.register(Post)
admin.site.register(Comment)