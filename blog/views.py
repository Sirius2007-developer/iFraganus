from django.shortcuts import render, get_object_or_404
from .models import Format, Team, Course
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from .forms import ConsultationForm, RegisterForm
# Create your views here.
def index(request):
    consult = ConsultationForm(request.POST or None)
    if request.method == "POST" and consult.is_valid():
        consult.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli tarzda yuborildi!")
    regist = RegisterForm(request.POST or None)
    if request.method == "POST" and regist.is_valid():
        regist.save()
        return HttpResponse("<h1>So'rovingiz amalga oshirildi!")
    format = Format.objects.all()
    context = {
        "format": format,
        "consult": consult,
    }
    return render(request, "index.html", context=context)


def formatdetailview(request, format):
    format = get_object_or_404(Format, slug=format)
    context = {
        "format": format,
    }
    return render(request, "Format/formatdetail.html", context=context)

class formatUpdateView(UpdateView):
    model = Format
    fields = "__all__"
    template_name = "Format/formatEdit.html"

class formatDeleteView(DeleteView):
    model = Format
    template_name = "Format/formatDelete.html"
    success_url = reverse_lazy('index')

class formatCreateView(CreateView):
    model = Format
    fields = "__all__"
    template_name = "Format/formatCreate.html"


# <!-----    Course       ------>
def coursedetailview(request, course):
    course = get_object_or_404(Course, slug=course)
    context = {
        "course": course,
    }
    return render(request, "Course/coursedetail.html", context=context)

class courseUpdateView(UpdateView):
    model = Course
    fields = "__all__"
    template_name = "Course/courseEdit.html"

class courseDeleteView(DeleteView):
    model = Course
    template_name = "Course/courseDelete.html"
    success_url = reverse_lazy('index')

class courseCreateView(CreateView):
    model = Course
    fields = "__all__"
    template_name = "Course/courseCreate.html"




# <!-----    Team       ------>
def teamdetailview(request, team):
    team = get_object_or_404(Team, slug=team)
    context = {
        "team": team,
    }
    return render(request, "Team/teamdetail.html", context=context)

class teamUpdateView(UpdateView):
    model = Team
    fields = "__all__"
    template_name = "Team/teamEdit.html"

class teamDeleteView(DeleteView):
    model = Team
    template_name = "Team/teamDelete.html"
    success_url = reverse_lazy('index')

class teamCreateView(CreateView):
    model = Team
    fields = "__all__"
    template_name = "Team/teamCreate.html"
