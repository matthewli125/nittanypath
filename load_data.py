from django.conf import settings
import projectPhase2New.settings

settings.configure(INSTALLED_APPS = projectPhase2New.settings.INSTALLED_APPS, DATABASES = projectPhase2New.settings.DATABASES)

import django
django.setup()

from ntnyPth.models import *
from os import listdir
import csv


def csvToModel(path, fileName):
    File = open(path + fileName, "r")
    Schema = File.readline()[3:].replace("\n", "").split(",")
    dataFile = csv.reader(File)

    print("\n\n\n", Schema, "\n")

    for i in dataFile:
        stmt = fileName.split(".")[0] + "(" + ",".join(["{}=\"{}\"".format(Schema[j], i[j]) for j in range(len(Schema))]) + ")"


        inst = eval(stmt)
        print(stmt)
        inst.save()
    File.close()



if __name__ == "__main__":

    dataPth = "dataFiles/"

    # print schema and table sizes for debugging
    print("\n\n")
    for i in listdir(dataPth):
        file = open(dataPth+i, "r")
        schema = file.readline()[3:].replace("\n", "")
        print(i + ":" + " " * (30 - len(i)), schema + " "*(70-len(schema)), len(file.readlines()))
        file.close()
    print("\n\n")

    filesInOrder = ["Student.csv", "Professor.csv", "Department.csv", "Course.csv",
                    "Section.csv", "Enroll.csv", "Prof_teaching_team.csv", "TA_teaching_team.csv",
                    "Homework.csv", "Exam.csv", "Exam_grade.csv", "Post.csv", "Comment.csv"]


    # models = Student._meta.fields.pop
    # print(models)
    # # Student.create(email="ah3078@nittany.edu",
    # #                password="a1uqkqum",
    # #                name="Alicia Harber",
    # #                age="22",
    # #                gender="F",
    # #                major="MATH",
    # #                street="83 Corona Street",
    # #                zipcode="62684")

    a = Student.objects.get(pk="ak9804@nittany.edu")
    print(a.zipcode)
