from django.shortcuts import render, get_object_or_404, redirect
from .models import blogEntries


def displayblogs(request):
    blogs = blogEntries.objects.all()
    return render(request,'blogs/blogdisplay.html',{'blogs' : blogs})

def blogdetaileddisplay(request,blog):
    enquiry = get_object_or_404(blogEntries, id=blog)
    details = {"title" : enquiry.title, "content" : enquiry.content,"datecreated" : enquiry.datecreated,"author":enquiry.author}
    return render(request,'blogs/detaileddisplay.html',{'details'  : details})


def blogentry(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        datecreated = request.POST.get('ddate')
        author = request.POST.get('author')
        entry = blogEntries(title=title,content=content,datecreated=datecreated,author=author)
        entry.save()
        return redirect("simpledisplayblog")
    return render(request,"blogs/blogentry.html")

def blogdelete(request,id):
    enquiry = get_object_or_404(blogEntries,id=id)
    enquiry.delete()
    return redirect("simpledisplayblog")

def blogedit(request,id):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        datecreated = request.POST.get('ddate')
        author = request.POST.get('author')
        enquiry = get_object_or_404(blogEntries,id=id)
        enquiry.title = title
        enquiry.content = content
        enquiry.datecreated = datecreated
        enquiry.author = author
        enquiry.save()
        return redirect("simpledisplayblog")
    en = get_object_or_404(blogEntries,id=id)
    return render(request,"blogs/blogedit.html",{'en':en})