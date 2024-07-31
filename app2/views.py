from django.shortcuts import render
from django.http import HttpResponse
from .models import Register


def room(request):
    return render(request,"room.html")

def aboutus(request):
    return render(request,"aboutus.html")

def patient(request):
    return render(request,"patient.html")

def visited(request):
    return render(request,"visited.html")
    
def contactus(request):
    return render(request,"contactus.html")

def actionHCG(request):
    email=request.GET['Mail']
    #firstname=request.GET['firstname']
    subject=request.GET['subject']
    hospitalname=request.GET['HospitalName']
    contact=request.GET['Phoneno']
    
    r=Register()
    r.email=email
    #r.firstname=firstname
    r.subject=subject
    r.hospitalname=hospitalname
    r.contact=contact
    r.save()
    return render(request,"contactus.html",{"msg":"Successfully Submitted"})

def view(request):
    email=request.GET['Mail']
    Name=request.GET['Name']
    UMR=request.GET['UMR']
    r=Register()
    r.email=email
    r.Name=Name
    r.UMR=UMR
    r.save()
    return render(request,"visited.html",{"msg":"Successfully Submited"})
    
"""
    r=None
    try:
        r=Register.objects.get(email=email)
        print("r=",r)
    except Exception as ex:
        print(ex)
        return render()
    print(r!=None)
    if(r.design=="UMR")
        return redirect("")
        return render(request,"patient.html",{"msg":"Invalid Email-ID"})
"""



