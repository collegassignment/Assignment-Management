from django.urls import path
from college import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.views import PasswordResetView,PasswordChangeView
from django.contrib.auth.views import (
   
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
urlpatterns = [
    path('home/',views.homeview),
    path('contact/',views.contactview.as_view()),
    path('insertcontact/',views.insertcontact),
    path('insertsubscribe/',views.insertsubscribe),
    path('faq/',views.faqview),
    path('signup/',views.signup),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('loginstudent/',views.loginstudent),
    path('blog/<int:id>',views.blogview),
    path('accounts/password_reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('accounts/reset/done/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    
]
   
   

