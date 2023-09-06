from django.shortcuts import render
from django.http import JsonResponse
from .models import District,Taluk,Blood_bank

# Create your views here.

def common_index(request):
    return render(request,'common_templates/index.html')

def about(request):
    return render(request,'common_templates/about.html')

def blog(request):
    return render(request,'common_templates/blog.html')

def contact(request):
    return render(request,'common_templates/contact.html')

def  bms_details(request):
    return render(request,'common_templates/what_is_bms.html')

def  login(request):
    return render(request,'common_templates/common_login.html')

def  register(request):
    return render(request,'common_templates/register_to_donate.html')

def  taluk(request):
    
    dis_id = request.POST['dis_id']
 
    taluk = Taluk.objects.filter(district_id = dis_id)
    blood_bank = Blood_bank.objects.filter(dist_id =dis_id)
    print(taluk)
    
    serialized_set = [{'t_name':t.name} for t in taluk]
    
    serialized_blood_bank = [{'b_name':b.bank_name} for b in blood_bank]
    
    return JsonResponse({'taluk':serialized_set,'blood_bank':serialized_blood_bank})

