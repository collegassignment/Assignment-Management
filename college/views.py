from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from college.forms import *
from django.contrib.auth import login, authenticate

# Create your views here.
class loginview(TemplateView):
    template_name="login.html"

class contactview(TemplateView):
    template_name="contact.html"

def insertcontact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/')
    else:
        form=contactform()
    return render(request,"contact.html",{'form':form})

def insertsubscribe(request):
    if request.method=='POST':
        form=subscribeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form=subscribeform()
    return render(request,"base.html",{'form':form})
def homeview(request):
    courses=course.objects.all()
    events=event.objects.all()
    blg=blog.objects.all()
    return render(request,"home.html",{'courses':courses,'events':events,'blg':blg})
def faqview(request):
     faqs=faq.objects.all()
     return render(request,"faq.html",{'faqs':faqs})
def signup(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            User=form.save()
            login(request,User)
            return redirect('/profiledetail/')
    else:
        form=signupform()
    return render(request,"registration/signup.html",{'form':form})

def loginstudent(request):
    
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                )
            login(request,user)
            return redirect('/studash/')
def blogview(request,id):
    b=blog.objects.get(id=id)
    return render(request,"blog.html",{'b':b})

