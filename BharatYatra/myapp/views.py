from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        nationality = request.POST['nationality']
        message = request.POST['message']
        print(name, email, phone, nationality, message)

        if len(name) < 2 or len(email) < 3 or len(phone) < 10:
            messages.error(request, "Please fill form correctly.")
        else:
            messages.success(request, "Your Message has been successfully sent!")
        contact = Contact(name=name, email=email, phone=phone, nationality=nationality, message=message)
        contact.save()
    return render(request, "myapp/index.html", {})


def resort(request):
    return render(request, "myapp/resort.html", {})


def packages(request):
    return render(request, "myapp/packages.html", {})
