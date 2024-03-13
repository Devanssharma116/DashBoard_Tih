from django.shortcuts import render,redirect
from django.http import HttpResponse 
from panel.models import *

def receipts(request):
    if request.method == 'POST':
        data = request.POST
        fname = data.get('fname')
        mail =data.get('mail')
        dob = data.get('dob')
        phone = data.get('phone')
        p_phone = data.get('p_phone')
        address = data.get('address')

        student.objects.create(
            fname = fname,
            mail = mail,
            dob = dob,
            phone = phone,
            p_phone = p_phone,
            address = address
        )
        return redirect('/SD/')
    return render(request,"Student_Details.html")

def table1(request):
    a = student.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'index.html',contextmenu)

def table2(request):
    a = student.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'StudentData.html',contextmenu)

def delete(request,id):
    a = student.objects.get(id=id)
    a.delete()
    return redirect('/table/')

def letureAdd(request):
    if request.method == 'POST':
        data = request.POST
        tname = data.get('tname')
        # upfile =data.get('upfile')
        up = data.get('up')

        Leture.objects.create(
            tname = tname,
            up = up,
            # upfile = upfile
        )
        return redirect('/panel/LA/')
    return render(request,"LectureAdd.html")


def letureShow(request):
    a = Leture.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'LectureShow.html',contextmenu)

def delete1(request,id):
    a = Leture.objects.get(id=id)
    a.delete()
    return redirect('/LS/')


# def courseHAdd(request):
#     if request.method == 'POST':
#         data = request.POST
#         tname = data.get('tname')
#         # upfile =data.get('upfile')
#         up = data.get('up')

#         CourseH.objects.create(
#             tname = tname,
#             up = up,
#             # upfile = upfile
#         )
#         return redirect('/CHA/')
#     return render(request,"courseHTML_Add.html")


# def courseHShow(request):
#     a = CourseH.objects.all()
#     contextmenu={
#         'table':a
#     }
#     return render(request,'courseHTML_Show.html',contextmenu)

# def deleteH(request,id):
#     a = CourseH.objects.get(id=id)
#     a.delete()
#     return redirect('/CHS/')

def courseAdd(request):
    if request.method == 'POST':
        data = request.POST
        tname = data.get('tname')
        # upfile =data.get('upfile')
        up = data.get('up')

        Course.objects.create(
            tname = tname,
            up = up,
            # upfile = upfile
        )
        return redirect('/CA/')
    return render(request,"add_course.html")

def courseshow(request):
    a=Course.objects.all()
    contextmenu={
        'table':a
        
    }
    return render(request,'show_course.html',contextmenu)

def deleteJ(request,id):
    a = Course.objects.get(id=id)
    a.delete()
    return redirect('/CJS/')

def AssignAdd(request):
    if request.method == 'POST':
        data = request.POST
        tname = data.get('tname')
        # upfile =data.get('upfile')
        up = data.get('up')
        titles = data.get('titles')
        des = data.get('des')
        asgn = data.get('asgn')

        Assignment.objects.create(
            tname = tname,
            up = up,
            asgn = asgn,
            titles = titles,
            des = des,
            # upfile = upfile
        )
        return redirect('/panel/AA/')
    return render(request,"AssignmentAdd.html")


def AssignShow(request):
    a = Assignment.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'AssignmentShow.html',contextmenu)




def deleteA(request,id):
    a = Assignment.objects.get(id=id)
    a.delete()
    return redirect('/AS/')


def NotesAdd(request):
    if request.method == 'POST':
        data = request.POST
        tname = data.get('tname')
        # upfile =data.get('upfile')
        up = data.get('up')

        Notes.objects.create(
            tname = tname,
            up = up,
            # upfile = upfile
        )
        return redirect('/NA/')
    return render(request,"NotesAdd.html")


def NotesShow(request):
    a = Notes.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'NotesShow.html',contextmenu)

def deleteN(request,id):
    a = Notes.objects.get(id=id)
    a.delete()
    return redirect('/NS/')

def TestAdd(request):
    if request.method == 'POST':
        data = request.POST
        tname = data.get('tname')
        # upfile =data.get('upfile')
        up = data.get('up')

        Tests.objects.create(
            tname = tname,
            up = up,
            # upfile = upfile
        )
        return redirect('/TA/')
    return render(request,"TestseriesAdd.html")


def TestShow(request):
    a = Tests.objects.all()
    contextmenu={
        'table':a
    }
    return render(request,'TestseriesShow.html',contextmenu)



def deleteT(request,id):
    a = Tests.objects.get(id=id)
    a.delete()
    return redirect('/TS/')