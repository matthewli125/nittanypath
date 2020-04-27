from django.conf import settings
import projectPhase2New.settings
from tqdm import tqdm

settings.configure(INSTALLED_APPS = projectPhase2New.settings.INSTALLED_APPS, DATABASES = projectPhase2New.settings.DATABASES)

import django
django.setup()

from django.contrib.auth.models import User
from ntnyPth.models import Student, Professor

students = [User.objects.create_user(i.email, i.email, i.password) for i in tqdm(Student.objects.all())]
# professors = [User.objects.create_user(i.email, i.email, i.password) for i in tqdm(Professor.objects.all())]

for i in students:
    i.groups.add(1)

# for i in professors:
#     i.groups.add(2)