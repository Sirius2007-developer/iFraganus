from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Consultation)
admin.site.register(Time_lesson)
admin.site.register(Lesson)
admin.site.register(Date)
admin.site.register(Header)
admin.site.register(Faq)
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}







