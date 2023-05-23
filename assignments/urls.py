from django.urls import path
from assignments import views
from django.contrib.auth import views as  auth_views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import (
   
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
     path('dashboard/',views.dashboardview),
     path('teacherlogin/',LoginView.as_view(),name="login"),
     path('logout/',LogoutView.as_view(),name="logout"),
     path('assignment/<int:id>/<int:cid>/<int:sid>',views.assignmentview),
     path('news/<int:id>',views.newsview),
     path('regstu/<int:id>',views.regstuview),
     path('unchkassign/<int:sid>',views.unchkassignview),
     path('chkassign/<int:sid>',views.chkassignview),
     path('stunewassign/<int:cid>/<int:sid>',views.stunewassignview),
     path('stuuploadassign/<int:id>',views.stuuploadassignview),
     path('profile/',views.profileview),
     path('stuprofile/',views.stuprofileview),
     path('studash/',views.studashview),
     path('edit/',views.editview),
     path('profiledetail/',views.profiledetailview),
     path('insertprofile/',views.insertprofile),
     path('insertassignment/',views.insertassignment),
     path('insertnews/',views.insertnews),
     path('deletenews/<int:id>',views.deletenews),
     path('deleteassign/<int:id>',views.deleteassign),
     path('editnews/<int:id>',views.editnews),
     path('updatenews/<int:id>',views.updatenews),
     path('editassign/<int:id>',views.editassign),
     path('updateassign/<int:id>',views.updateassign),
     path('updateprofile/<int:id>',views.updateprofile),
     path('newupdate/<int:id>/<int:stuid>',views.newupdateview),
     path('uploadupdate/<int:id>',views.uploadupdateview),
     path('insertfile/',views.insertfile),
     path('updateunchk/<int:id>',views.updateunchk),
     path('teachunchk/',views.teachunchk),
     path('teachunchkview/<int:id>',views.teachunchkview),
     path('getassignment/<int:id>',views.getassignmentview),
     path('getassign/<int:id>',views.getassignview),
     path('teachchk/',views.teachchk),
     path('teachchkview/<int:id>',views.teachchkview),
     path('change_password/',views.change_passswordview,name='change_password'),
     path('changepassword/',views.changepasswordview,name="change_password"), 
     path('assignedit/',views.assigneditview),
     path('editstuassign/<int:id>',views.editstuassign),
     path('updatestuassign/<int:id>',views.updatestuassign),
     path('subjectwise/<int:sid>',views.subjectwiseview),
     path('fetchassign/',views.fetchassignview),
     path('getassign/',views.getassign),
]
    