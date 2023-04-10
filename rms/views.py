from django.shortcuts import render,redirect
from django.views.generic import CreateView,View
from .models import *
from .forms import *
from django.contrib.auth import login
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login , logout
from django.utils.decorators import method_decorator

class HomePageView(View):
    def get(self,req):
        return render(req,"home.html")
    
@method_decorator([login_required, student_required],name='dispatch')
class Student(View):
    def get(self,req):
        return render(req,"singup/student.html")
class StudentSingupView(CreateView):
    model=User
    form_class=StudentSingupForm
    template_name="singup/register.html"
    success_url="/singup/"
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("student")
    
    
@method_decorator([login_required, teacher_required],name='dispatch')
class Teacher(View):
    def get(self,req):
        return render(req,"singup/teacher.html")   
class TeacherSingupView(CreateView):
    model=User
    form_class=TeacherSingupForm
    template_name="singup/register.html"
    success_url="/singup/"
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("teacher")
# def login(req):
#     LoginForm = AuthenticationForm(data=req.POST or None)
#     if req.method =="POST":
#         if LoginForm.is_valid():
#             username = LoginForm.cleaned_data.get('username')
#             password = LoginForm.cleaned_data.get("password")
#             user = authenticate(username = username , password=password)
#             if user is not None:
#                 print(user)
#                 login(req,user)
#                 return redirect("teacher")
#             else:
#                 return redirect(login)
#     return render(req,"Patient/login.html",{"form":LoginForm})
@login_required
def logout(req):
    logout(req)
    return redirect(login)


class SingUp(View):
    def get(self,req):
        return render(req,"singup/index.html")

