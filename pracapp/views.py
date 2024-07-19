from django.shortcuts import render, get_object_or_404, redirect
from .models import contactEnquiry

def saveform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        sname = request.POST.get('sname')
        en = contactEnquiry(name=name, email=email, surname=sname)
        en.save()
        return redirect('displayform')
    return render(request, 'enquiryform.html')

def displayform(request):
    enquiries = contactEnquiry.objects.all()
    return render(request, 'display.html', {'enquiries': enquiries})

def editenquiry(request, id):
    enquiry = get_object_or_404(contactEnquiry, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        sname = request.POST.get('sname')
        enquiry.name = name
        enquiry.email = email
        enquiry.surname = sname
        enquiry.save()
        return redirect('displayform')
    return render(request, 'editform.html', {'enquiryreq': enquiry})

def deleteenquiry(request, id):
    enquiry = get_object_or_404(contactEnquiry, id=id)
    enquiry.delete()
    return redirect('displayform')
