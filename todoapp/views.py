from django.shortcuts import render, get_object_or_404, redirect
from .models import todoEntries


def displaytodos(request):
    todos = todoEntries.objects.all()
    return render(request,'todos/tododisplay.html',{'todos' : todos})

def tododetaileddisplay(request,todo):
    enquiry = get_object_or_404(todoEntries, id=todo)
    details = {"name" : enquiry.name, "description" : enquiry.description,"duedate" : enquiry.duedate,"status":enquiry.completionstatus}
    return render(request,'todos/detaileddisplay.html',{'details'  : details})


def todoentry(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        duedate = request.POST.get('date')
        entry = todoEntries(name=name,description=description,duedate=duedate)
        entry.save()
        return redirect("simpledisplay")
    return render(request,"todos/todoentry.html")

def tododelete(request,id):
    enquiry = get_object_or_404(todoEntries,id=id)
    enquiry.delete()
    return redirect("simpledisplay")

def todoedit(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('desc')
        duedate = request.POST.get('ddate')
        status = request.POST.get('status')
        enquiry = get_object_or_404(todoEntries,id=id)
        enquiry.name = name
        enquiry.description = description
        enquiry.duedate = duedate
        enquiry.completionstatus = status
        enquiry.save()
        return redirect("simpledisplay")
    en = get_object_or_404(todoEntries,id=id)
    return render(request,"todos/todoedit.html",{'en':en})