from django.db import models
from tinymce.models import HTMLField

# Create your models here.
Sem=(
    ('Sem1','Sem1'),
    ('Sem3','Sem3'),
    ('Sem5','Sem5')

)
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.IntegerField()
    message=models.TextField()
    class Meta:
        db_table="contact"
    def __str__(self):
        return self.name
   

class event(models.Model):
    date=models.DateField()
    name=models.CharField(max_length=100)
    name1=models.CharField(max_length=100)
    info=models.TextField()
    photo=models.ImageField(upload_to='event/')
    class Meta:
        db_table="event"
    def __str__(self):
        return self.name

class blog(models.Model):
    photo=models.ImageField(upload_to='blog/')
    title=models.CharField(max_length=100)
    description=HTMLField()
    postby=models.CharField(max_length=100)
    poston=models.DateField()
    class Meta:
        db_table="blog"
    def __str__(self):
        return self.title
class course(models.Model):
    Pic=models.ImageField()
    Coursename=models.CharField(max_length=100)
    Description=models.TextField()
    class Meta:
        db_table="course"
    def __str__(self):
        return self.Coursename
class subscribe(models.Model):
    email=models.CharField(max_length=100)
    class Meta:
        db_table="subscribe"
    def __str__(self):
        return self.email
class faq(models.Model):
    question=models.TextField()
    answer=models.TextField()
    class Meta:
        db_table="faq"
    def __str__(self):
        return self.question


