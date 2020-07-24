"""project6 URL Configuration

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
from django.urls import path
from app6 import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="welcome.html"),name="main"),
    path('Admin_login/',TemplateView.as_view(template_name="adminlogin.html"),name="alogin"),
    path('Check_Credentials/',views.Check_Credentials,name="Check_Credentials"),
    path('adminmain/',views.Adminmain,name="adminmain"),
    path('addcourse/',views.AddCourse.as_view(),name="addcourse"),
    path('viewcourse/',views.Courseinfo.as_view(),name="viewcourse"),
    path('update_course<int:pk>/', views.Update_info.as_view(), name="update_course"),

    path('full_details<int:pk>/', views.ShowFullDetails.as_view(), name="full_details"),

    path('delete_course<int:pk>/', views.DeleteEmployee.as_view(), name="delete_course"),

    path('student_register/',views.StudentRegister.as_view(),name="student_register"),

    path('approve_students/',views.ApproveStudents.as_view(),name="approve_students"),

    path('reject/',views.Reject,name="Reject"),

    path('approve/',views.approve,name="approve"),

    path('View_approve_users/',views.ViewApproveUsers.as_view(),name="View_approve_users"),

    path('student_login/',TemplateView.as_view(template_name="student_login.html"),name="student_login"),

    path('Check_details/',views.CheckDetails,name="Check_details"),

    path('viewcoursedetails/',views.Viewcoursedetails.as_view(),name="viewcoursedetails"),

    path('enrollcourse/', views.EnrollCourse, name="enrollcourse"),

    path('fulldetails<int:pk>/', views.ShowCourseDetails.as_view(), name="fulldetails"),

    path('studentmain/',views.Studentmain,name="studentmain"),

    path('viewenrollments/',views.Viewenrollments.as_view(),name="viewenrollments"),

    path('save_course/', views.save_course, name="save_course"),

    path('CheckCourseName/', views.CheckCourseName, name="CheckCourseName"),

    path('CheckFacultyName/', views.CheckFacultyName, name="CheckFacultyName"),

    path('save_student/',views.save_student,name="save_student"),

    path('CheckName/', views.CheckName, name="CheckName"),

    path('CheckContact/', views.CheckContact, name="CheckContact"),

    path('CheckEmail/',views.CheckEmail,name="CheckEmail")


]
