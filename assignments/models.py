from django.db import models
from college.models import *
from django.contrib.auth.models import User
import datetime

# Create your models here.
Gender=(
    ('Male','Male'),
    ('Female','Female')
)
Sem=(
    ('Sem1','Sem1'),
    ('Sem2','Sem2'),
    ('Sem3','Sem3'),
    ('Sem4','Sem4'),
    ('Sem5','Sem5')

)

class teacherprofile(models.Model):
    
    Photo=models.ImageField(upload_to='teacherprofile/')
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100, choices=Gender)
    Contact=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Course_id=models.ForeignKey(course, on_delete=models.CASCADE)
    Address=models.TextField(default='')
    Dateofjoin=models.DateField(default='')
    Teacher_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        db_table="teacherprofile"
    def __str__(self):
        return self.Name
class subject(models.Model):
    Course_id=models.ForeignKey(course,on_delete=models.CASCADE)
    Semester=models.CharField(max_length=100 ,default='')
    Subjectname=models.CharField(max_length=100)
    Subjectcode=models.CharField(max_length=100 ,default='')
    class Meta:
        db_table="subject"
    def __str__(self):
        return self.Subjectname
class studentprofile(models.Model):
    
    Student_id=models.ForeignKey(User, on_delete=models.CASCADE,default='')
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    Course_id=models.ForeignKey(course, on_delete=models.CASCADE,default='')
    Sem=models.CharField(max_length=100 ,default='')
    Rollno=models.IntegerField()
    Registration_no=models.CharField(max_length=100,default='')
    class Meta:
        db_table="studentprofile"
    def __str__(self):
        return self.First_name
    
class new(models.Model):
    Teacherprofile_id=models.ForeignKey(teacherprofile, on_delete=models.CASCADE)
    Title=models.CharField(max_length=100)
    Description=models.TextField()
    Date=models.DateField(default=datetime.date.today())
    class Meta:
        db_table="news"
    def __str__(self):
        return self.Title
class assignment(models.Model):
    Teacherprofile_id=models.ForeignKey(teacherprofile, on_delete=models.CASCADE)
    Course_id=models.ForeignKey(course, on_delete=models.CASCADE)
    Sem=models.CharField(max_length=100,default='')
    Subject_id=models.ForeignKey(subject, on_delete=models.CASCADE,related_name="subjects",default='')
    Assignment_Number=models.IntegerField()
    Assignment_Title=models.CharField(max_length=100)
    Assignment_Description=models.CharField(max_length=100)
    Submission_Date=models.DateField()
    Assignment_Marks=models.IntegerField()
    Assignment_File=models.FileField(upload_to='assignment/')
    class Meta:
        db_table="assignment"
    def __str__(self):
        return self.Assignment_Title
class uploads(models.Model):
    Assignment_id=models.ForeignKey(assignment, on_delete=models.CASCADE)
    Student_id=models.ForeignKey(studentprofile, on_delete=models.CASCADE)
    Status=models.CharField(max_length=100,default="unchecked")
    Marks=models.FloatField(default="0")
    Remarks=models.CharField(max_length=100)
    Assignment_File=models.FileField(upload_to='uploaded')
    Assignment_Description=models.CharField(max_length=100,default='')
    Submission_Date=models.DateField(default=datetime.date.today())

    class Meta:
        db_table="uploads"
    def __str__(self):
        return self.Status
