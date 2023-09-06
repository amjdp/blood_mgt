from django.shortcuts import render

# Create your views here.

def patient_index(request):
    return render(request,'patient_templates/index.html')

def about(request):
    return render(request,'patient_templates/about.html')

def blog(request):
    return render(request,'patient_templates/blog.html')

def contact(request):
    return render(request,'patient_templates/contact.html')

def  bms_details(request):
    return render(request,'patient_templates/what_is_bms.html')

