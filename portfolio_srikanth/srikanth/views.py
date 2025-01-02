from django.shortcuts import render,redirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from django.conf import settings
import os 
from .models import Project,Contact,certificates
from django.core.mail import send_mail


def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html") 


def resume(request):
    resume_path = os.path.join(settings.BASE_DIR, 'folder', 'resume.pdf')  
    if os.path.exists(resume_path):
        with open(resume_path, 'rb') as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
            return response
    else:
        return HttpResponse("Resume not found", status=404) 
    

def project_list(request):
    projects = Project.objects.all() 
    return render(request, 'projects.html', {'projects': projects})

def contact1(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("message")
        
        if not all([Name, Email, number, message]):
            return HttpResponse("Please fill all details.")
        
        try:
            contact = Contact(Name=Name, Email=Email, number=number, message=message)
            contact.save()

            send_mail(
                subject=f"Contact Form Submission from {Name}",
                message=f"Name: {Name}\nEmail: {Email}\nNumber: {number}\n\nMessage:\n{message}",
                from_email="srikanthirupathaiah@gmail.com",  # Use settings.EMAIL_HOST_USER
                recipient_list=[Email],  
                fail_silently=False,
            )

            send_mail(
                subject="Thank you for contacting us!",
                message=f"Hi {Name},\n\nThank you for reaching out! We have received your message and will get back to you soon.\n\nBest regards,\nYour Team",
                from_email="srikanthirupathaiah@gmail.com", 
                recipient_list=[Email],
                fail_silently=False,
            )

            return render(request, "success.html")
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")

    return render(request, "contact.html")


def certificate(request):
    certi = certificates.objects.all()  # Fetch all certificates from the database
    return render(request, "about.html", {'ci': certi})



def certificate(request):
    c=Project.objects.all()
    return render(request,"about.html",{'c':c})



