from django.contrib import admin
from college.models import *
# Register your models here.
@admin .register(contact)
class contactadmin(admin.ModelAdmin):
    list_display=('name','email','phone','message')

@admin.register(event)
class eventadmin(admin.ModelAdmin):
    pass
@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    pass
@admin.register(course)
class courseadmin(admin.ModelAdmin):
    pass
@admin.register(subscribe)
class subscribeadmin(admin.ModelAdmin):
    list_display=('email',)
@admin.register(faq)
class faqadmin(admin.ModelAdmin):
    pass




