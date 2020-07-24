from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView,TemplateView,View
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.models import User
from app6.models import CourseModel,StudentModel,EnrollModel
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse


def Check_Credentials(request):
    name = request.POST.get("uname")
    pwd = request.POST.get("pwd")

    if name == "krishna" and pwd == "krishna":
        return redirect("adminmain")


def Adminmain(request):
    return render(request,"adminwelcome.html")


class AddCourse(TemplateView):
    template_name = "Course_registration.html"
    # model = CourseModel
    # fields = "__all__"
    # success_url = "/addcourse/"
    # success_message = "Course details have been saved successfully"

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

class StudentRegister(TemplateView):
    template_name = "Studentregistration.html"
    # model = StudentModel
    # fields = "__all__"
    # success_url = "/student_register/"
    # success_message = "Your details have been saved please wait for approval"

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
    na = result.name
    if result.status == "Active" and result.emailid == ema and result.password == pwd:
        return redirect("studentmain")
    else:
        return redirect('student_login')


class Viewcoursedetails(ListView):
    template_name = "Coursedetails.html"
    model = CourseModel
    queryset = CourseModel.objects.values('idno', 'coursename', 'facultyname', 'stardate').order_by('idno')


class ShowCourseDetails(DetailView):
    template_name = "fulldetails.html"
    model = CourseModel


def EnrollCourse(request):
    no = request.GET.get("id")
    try:
        pm = CourseModel.objects.get(idno=no)
        no = pm.idno
        cna = pm.coursename
        fna = pm.facultyname
        fee = pm.fees
        stdate = pm.stardate
        dura = pm.duration
        ctime = pm.classtime
        EnrollModel(idno=no, coursename=cna, facultyname=fna,fees=fee, stardate=stdate, duration=dura,classtime=ctime).save()
        messages.success(request, "you have enrolled to course successflly")
        return redirect('viewcoursedetails')

    except IntegrityError:
        messages.error(request,"already Course has been enrolled")
        return redirect('viewcoursedetails')


def Studentmain(request):
    return render(request, "userwelcome.html")


class Viewenrollments(ListView):
    template_name = "Emrolledcoures.html"
    model = EnrollModel
    queryset = EnrollModel.objects.values('idno', 'coursename', 'facultyname', 'stardate','fees','duration','classtime').order_by('idno')

def save_course(request):
    cname = request.POST.get("t1")
    fname = request.POST.get("t2")
    fee = request.POST.get("t3")
    sdate = request.POST.get("t4")
    dura = request.POST.get("t5")
    ctime = request.POST.get("t6")
    CourseModel(coursename=cname,facultyname=fname,fees=fee,stardate=sdate,duration=dura,classtime=ctime).save()
    messages.success(request,"Course details have been saved successfully")
    return redirect("addcourse")

@method_decorator(csrf_exempt,name='dispatch')
def CheckCourseName(request):
    name = request.POST.get("cname")
    print(name)
    try:
        CourseModel.objects.get(coursename=name)
        res = {"error":"Name is already taken"}
    except CourseModel.DoesNotExist:
        res = {"mess":"Name is available"}
    return JsonResponse(res)

@method_decorator(csrf_exempt,name='dispatch')
def CheckFacultyName(request):
    name = request.POST.get("cname")
    print(name)
    try:
        CourseModel.objects.get(facultyname=name)
        res = {"error": "Faculty is not free"}
    except CourseModel.DoesNotExist:
        res = {"mess": "Faculty is available"}
    return JsonResponse(res)


def save_student(request):
    sname = request.POST.get("t1")
    contact = request.POST.get("t2")
    ema = request.POST.get("t3")
    password = request.POST.get("t4")
    stat = request.POST.get("t5")
    StudentModel(name=sname,contactnumber=contact,emailid=ema,password=password,status=stat).save()
    messages.success(request, "Your details have been saved please wait for approval")
    return redirect("student_register")

@method_decorator(csrf_exempt,name='dispatch')
def CheckName(request):
    name = request.POST.get("cname")
    print(name)
    try:
        StudentModel.objects.get(name=name)
        res = {"error":"Username with this name is already taken"}
    except StudentModel.DoesNotExist:
        res = {"mess":"Name is available"}
    return JsonResponse(res)

@method_decorator(csrf_exempt,name='dispatch')
def CheckContact(request):
    contact = request.POST.get("cname")
    print(contact)
    try:
        StudentModel.objects.get(contactnumber=contact)
        res = {"error": "This number is already used"}
    except StudentModel.DoesNotExist:
        res = {"mess": "This number is available"}
    return JsonResponse(res)

@method_decorator(csrf_exempt,name='dispatch')
def CheckEmail(request):
    email = request.POST.get("cname")
    print(email)
    try:
        StudentModel.objects.get(emailid=email)
        res = {"error":"Email id is already taken"}
    except StudentModel.DoesNotExist:
        res = {"mess":"Email id is available"}
    return JsonResponse(res)