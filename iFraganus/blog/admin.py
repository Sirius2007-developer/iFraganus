from django.contrib import admin
from .models import Format, Consultation, Course, Team
# Register your models here.
admin.site.register(Consultation)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}




