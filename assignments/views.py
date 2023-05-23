from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.views.generic import TemplateView
from college.models import *
from assignments.models import *
from assignments.forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required
def dashboardview(request):
    userid=request.user.id
    td=teacherprofile.objects.get(Teacher_id_id=userid)
    students = studentprofile.objects.filter(Course_id_id=td.Course_id).count()
    assignments=assignment.objects.filter(Teacherprofile_id_id=td.id).count()
    news = new.objects.filter(Teacherprofile_id_id=td.id).count()
    context = {'students': students,'assignments':assignments,'news':news
        }
    return render(request,"dashboard.html",context)

def assignmentview(request,id,cid,sid):
     courses=course.objects.filter(id=cid)
     subjects=subject.objects.filter(Course_id_id=sid)
     assignments=assignment.objects.filter(Teacherprofile_id_id=id)
     context={'courses':courses,'subjects':subjects,'assignments':assignments}
     return render(request,"assignment.html",context)

def newsview(request,id):
    newss=new.objects.filter(Teacherprofile_id_id=id)
    context={'newss':newss}
    return render(request,"news.html",context)

def regstuview(request,id):
    rs=studentprofile.objects.filter(Course_id_id=id)
    return render(request,"regstu.html",{'rs':rs})
def unchkassignview(request,sid):
   subjects=subject.objects.filter(Course_id_id=sid)
   return render(request,"unchkassign.html",{'subjects':subjects})
def chkassignview(request,sid):
   subjects=subject.objects.filter(Course_id_id=sid)
   return render(request,"chkassign.html",{'subjects':subjects})
def stunewassignview(request,cid,sid):
    assignments=assignment.objects.filter(Course_id_id=cid,Sem=sid)
    courses=course.objects.all()
    subjects=subject.objects.all()
    students=studentprofile.objects.all()
    context={'subjects':subjects,'courses':courses,'assignments':assignments,'students':students}
    return render(request,"stunewassign.html",context)
def stuuploadassignview(request,id):
    #assign=assignment.objects.select_related('Subject_id')
    upload=uploads.objects.select_related('Assignment_id').filter(Student_id_id=id)
    return render(request,'stuuploadassign.html',{'upload':upload})
def profileview(request):
    return render(request,"profile.html")
def stuprofileview(request):
    courses=course.objects.all()
    # sems=studentprofile.objects.all()
    return render(request,'stuprofile.html',{'courses':courses})
def studashview(request):
    userid=request.user.id
    stu=studentprofile.objects.get(Student_id_id=userid)
    n=new.objects.select_related('Teacherprofile_id').filter(Teacherprofile_id__Course_id_id=stu.Course_id)
    return render(request,'studash.html',{'n':n})
def editview(request):
    return render(request,'edit.html')
def profiledetailview(request):
    c=course.objects.all()
    return render(request,"profiledetail.html",{'c':c})
def insertprofile(request):
    if request.method=='POST':
        form=profileform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/studash/')
        else:
            return HttpResponse("Failed To Insert Data!")
    else:
        form=profileform()
    return render(request,"profiledetail.html",{'form':form})
def insertassignment(request):
    if request.method=='POST':
        form=assignmentform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
            return redirect('/assignment/')
        else:
            return HttpResponse("Failed To Insert Data!")
    else:
        form=assignmentform()
    return render(request,"assignment.html",{'form':form})
def insertnews(request):
    if request.method=='POST':
        form=newform(request.POST)
        if form.is_valid():
            form.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
        else:
            return HttpResponse("Failed To Insert Data!")
    else:
        form=newform()
    return render(request,"news.html",{'form':form})
def deletenews(request,id):
    newss=new.objects.get(id=id)
    newss.delete()
    return redirect('/dashboard/')
def editnews(request,id):
    newss=new.objects.get(id=id)
    return render(request,'editnews.html',{'newss':newss})
def updatenews(request,id):
    newss=new.objects.get(id=id)
    form=newform(request.POST,instance=newss)
    if form.is_valid():
         form.save()
    return redirect('/dashboard/')
    return render(request,'editnews.html',{'form':form})
def editassign(request,id):
    assignments=assignment.objects.get(id=id)
    courses=course.objects.all()
    subjects=subject.objects.all()
    
    return render(request,'edit.html',{'assignments':assignments,'courses':courses,'subjects':subjects})
def deleteassign(request,id):
    assignments=assignment.objects.get(id=id)
    assignments.delete() 
    return redirect('/dashboard/')
def updateassign(request,id):
    assignments=assignment.objects.get(id=id)
    form=assignmentform(request.POST,request.FILES,instance=assignments)
    if form.is_valid():
         form.save()
    return redirect('/dashboard/')
    return render(request,'edit.html',{'form':form})

def updateprofile(request,id):
    s=studentprofile.objects.get(id=id)
    form=profileform(request.POST,instance=s)
    if form.is_valid():
         form.save()
         return redirect('/studash/')
    return render(request,'stuprofile.html',{'form':form})
def newupdateview(request,id,stuid):
    assign=assignment.objects.select_related('Subject_id').get(id=id)
    s=assign.Submission_Date
    
    d=datetime.today().date()

    
    try:
        up=uploads.objects.filter(Assignment_id_id=id,Student_id_id=stuid)
        a=assignment.objects.filter(id=id,Submission_Date__gte=d)
        context={'n':assign,'up':up,'a':a}
    except ObjectDoesNotExist:
        
        context={'n':assign}
   
    return render(request,"newupdate.html",context)

def uploadupdateview(request,id):
   upload=uploads.objects.get(id=id)
   return render(request,'uploadupdate.html',{'u':upload})


def insertfile(request):
    if request.method=='POST':
        form=uploadsform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/studash/')
        else:
            return HttpResponse('failed to insert data')
    else:
        form=uploadsform()
    return render(request,'newupdate.html',{'form':form})
def teachunchk(request):
    return render(request,'teachunchk.html')
def teachunchkview(request,id):
    u=uploads.objects.get(id=id)
    return render(request,'teachunchkview.html',{'u':u})

def updateunchk(request,id):
    u=uploads.objects.get(id=id)
    form=uploadsform(request.POST,request.FILES,instance=u)
    if form.is_valid():
         form.save()
         return redirect('/dashboard/')
    return render(request,'teachunchkview.html',{'form':form})



def getassignmentview(request,id):
    if request.method=='POST':
        subjectid=request.POST['Subject_id']
        data=uploads.objects.select_related('Assignment_id').filter(Status='unchecked',Assignment_id__Teacherprofile_id_id=id,Assignment_id__Subject_id_id=subjectid)
        return render(request,"teachunchk.html",{'data':data})
def getassignview(request,id):
    if request.method=='POST':
        subjectid=request.POST['Subject_id']
        data=uploads.objects.select_related('Assignment_id').filter(Status='checked',Assignment_id__Teacherprofile_id_id=id,Assignment_id__Subject_id_id=subjectid)
        return render(request,"teachchk.html",{'data':data})
def teachchk(request):
    return render(request,'teachchk.html')
def teachchkview(request,id):
    u=uploads.objects.get(id=id)
    return render(request,'teachchkview.html',{'u':u})

def change_passswordview(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('/studash/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
def changepasswordview(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {
        'form': form
    })

def assigneditview(request):
      # assignments=assignment.objects.get(id=vid)
    return render(request,'assignedit.html',context)

def editstuassign(request,id):
    upload=uploads.objects.get(id=id)
    courses=course.objects.all()
    subjects=subject.objects.all()
    d=datetime.today().date() 
    try:
        data=uploads.objects.select_related('Assignment_id').filter(id=id,Assignment_id__Submission_Date__gte=d)
        context={'data':data,'upload':upload,'courses':courses,'subjects':subjects}
    except ObjectDoesNotExist:
     context={'upload':upload,'courses':courses,'subjects':subjects}
    
    
    return render(request,'assignedit.html',context)

def updatestuassign(request,id):
    upload=uploads.objects.get(id=id)
    assignments=assignment.objects.all()
    form=uploadsform(request.POST,request.FILES,instance=upload)
    if form.is_valid():
         form.save()
    return redirect('/studash/')
def subjectwiseview(request,sid):
    # assignments=assignment.objects.filter(Submission_Date=)
    subjects=subject.objects.filter(Course_id_id=sid)
    return render(request,"subjectwise.html",{'subjects':subjects})
def fetchassignview(request):
    return render(request,"fetchassign.html")
def getassign(request):
    fromdate=request.POST.get("fromdate")
    todate=request.POST.get("todate")
    subject=request.POST.get("Subject_id")
    a=uploads.objects.select_related('Assignment_id').filter(Assignment_id__Submission_Date__range=(fromdate,todate),Assignment_id__Subject_id=subject)
    #a=assignment.objects.filter(Submission_Date__range=(fromdate,todate),Subject_id=subject)
    return render(request,"fetchassign.html",{'a':a})

