"""projectPhase2New URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='homepages/index.html'), name='home'),
    path('users/home', views.user_home, name='user_home'),
    path('users/classes/<str:name>/<str:course_id>', views.student_class_info, name='student_class_info'),
    path('users/manage/<str:name>/<str:course_id>/<str:sec_no>', views.prof_class_info, name='prof_class_info'),
    path('users/drop/<str:course_id>', views.drop_class, name='drop_class'),
    path('classes/add_assignment/<str:atype>/<int:anum>/<str:adet>', views.add_assignment, name='add_assignment'),
    path('classes/add_assignment/', views.add_assignment, name='add_assignment'),
    path('classes/del_assignment/<str:atype>/<int:anum>', views.delete_assignment, name='delete_assignment'),
    path('classes/del_assignment/', views.delete_assignment, name='delete_assignment'),
    path('view_dets/<str:atype>/<str:anum>', views.assignment_details, name='a_det'),
    path('view_dets/grade/<str:student_email>/<str:grade>/', views.create_grade, name='create_grade'),
    path('view_dets/grade/', views.create_grade, name='create_grade'),
    path('forum/<str:email>', views.posts, name='posts'),
    path('post/new', views.new_post, name='new_post'),
    path('forum/post/comment/new', views.new_comment, name='new_comment'),
    path('forum/detail/<int:pk>', views.post_detail, name='post_detail'),
    path('users/changepassword', views.change_password, name='change_password'),
    path('forum/announcements/all', views.announcements, name='announcements'),
    path('forum/announcements/new', views.new_announcement, name='new_announcement'),
    path('forum/announcements/details/<int:pk>', views.announcement_details, name='announcement_details')
]
