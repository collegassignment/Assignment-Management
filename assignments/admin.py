from django.contrib import admin
from assignments.models import *

# Register your models here.
@admin.register(teacherprofile)
class teachprofileadmin(admin.ModelAdmin):
    pass
@admin.register(subject)
class subjectadmin(admin.ModelAdmin):
    pass
@admin.register(studentprofile)
class studentprofileadmin(admin.ModelAdmin):
    pass
@admin.register(new)
class newsadmin(admin.ModelAdmin):
    pass
@admin.register(assignment)
class assignementadmin(admin.ModelAdmin):
    pass
@admin.register(uploads)
class uploadsadmin(admin.ModelAdmin):
    pass