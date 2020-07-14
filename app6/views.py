from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView,TemplateView,View
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.models import User
from app6.models import CourseModel,StudentModel

def Check_Credentials(request):
    name = request.POST.get("uname")
    pwd = request.POST.get("pwd")

    if name == "krishna" and pwd == "krishna":
        return redirect("adminmain")


def Adminmain(request):
    return render(request,"adminwelcome.html")


class AddCourse(SuccessMessageMixin,CreateView):
    template_name = "Course_registration.html"
    model = CourseModel
    fields = "__all__"
    success_url = "/addcourse/"
    success_message = "Course details have been saved successfully"

class Courseinfo(ListView):
    template_name = "Coursesinfo.html"
    model = CourseModel
    queryset = CourseModel.objects.values('idno','coursename','facultyname','stardate').order_by('idno')


class Update_info(UpdateView):
    template_name = "Update_course_details.html"
    model = CourseModel
    fields = "__all__"
    success_url = '/viewcourse/'



class ShowFullDetails(DetailView):
    template_name = "full_details.html"
    model = CourseModel


class DeleteEmployee(DeleteView):
    template_name = "confirm_delete_course.html"
    model = CourseModel
    success_url = '/viewcourse/'

class StudentRegister(SuccessMessageMixin,CreateView):
    template_name = "Studentregistration.html"
    model = StudentModel
    fields = "__all__"
    success_url = "/student_register/"
    success_message = "Your details have been saved please wait for approval"

class ApproveStudents(ListView):
    template_name = "viewstudents.html"
    model = StudentModel
    fields = "__all__"

def approve(request):
    no = request.GET.get("no")
    status = "Active"
    StudentModel.objects.filter(idno=no).update(status=status)
    return redirect('approve_students')


def Reject(request):
    no = request.GET.get("no")
    StudentModel.objects.filter(idno=no).delete()
    messages.success(request, "product added successfully")
    return redirect('approve_students')


class ViewApproveUsers(ListView):
    template_name = "viewapprovedstudents.html"
    model = StudentModel
    fields = "__all__"


def CheckDetails(request):
    ema = request.POST.get("eid")
    pwd = request.POST.get("pwd")
    result = StudentModel.objects.get(emailid=ema)
    if result.status == "Active" and result.emailid == ema and result.password == pwd:
        return render(request,"userwelcome.html",{"data":CourseModel.objects.all()})
    else:
        return redirect('student_login')
