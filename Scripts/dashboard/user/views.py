from django.shortcuts import render,redirect
from django.http import HttpResponse 
from panel.models import *

# Create your views here.
def table1s(request):
    a = student.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'StudentDatas.html',contextmenu)

def letureShows(request):
    a = Leture.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'LectureShows.html',contextmenu)

def courseHShows(request):
    a = CourseH.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'courseHTML_Shows.html',contextmenu)

def courseJShows(request):
    a = CourseJ.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'courseJS_Shows.html',contextmenu)

def AssignShows(request):
    a = Assignment.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'AssignmentShows.html',contextmenu)

def NotesShows(request):
    a = Notes.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'NotesShows.html',contextmenu)

def TestShows(request):
    a = Tests.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'TestseriesShows.html',contextmenu)





#### 