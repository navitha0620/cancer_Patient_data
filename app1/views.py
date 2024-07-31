from django.shortcuts import render,redirect

from .models import Register



def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")
    
def contact(request):
    return render(request,"contact.html")

def userhome(request):
    return render(request,"userhome.html")

def adminhome(request):
    return render(request,"adminhome.html")


def doregister(request):
    hospitalname=request.GET['HospitalName']
    contact=request.GET['Phoneno']
    email=request.GET['Mail']
    password=request.GET['Password']
   # department=request.GET['department']
    branchaddress=request.GET['branchaddress']
    #doctor=request.GET['doctor']
    
    
    r=Register()
    r.contact=contact
    r.hospitalname=hospitalname
    r.email=email
    r.branchaddress=branchaddress    
    r.password=password
    r.save()
    return render(request,"login.html",{"email":email})

def logincheck(request):
    email=request.GET['Mail']
    password=request.GET['Password']
    #department=request.GET['department']
    #hospitalname=request.GET['HospitalName']
    #contact=request.GET['Phoneno']
   # r=None
    try:
        r=Register.objects.get(email=email,password=password)
    #    print("r=",r)
    except Exception as ex:
   #     print(ex)
        return render(request,"login.html",{"msg":"Invalid Designation"})
    #if(r!=None):
     #   if(r.design=="user"):
      #      return redirect("/userhome")
       # if(r.design=="admin"):
        #    return redirect("/adminhome")
    #else:
     #   return render(request,"login.html",{"msg":"Invalid Designation"})
    #r=Register.objects.get(email=email)
    return render(request,"room.html")
    

def action(request):
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
    return render(request,"contact.html",{"msg":"Successfully Submitted"})

# Create your views here.

def viewuser(request):
    #all() returns all rows in an table as a register class objects
    user=Register.objects.all()
    return render(request,"viewuser.html",{"user":user})


def modify(request):
    operations=request.GET['operations']
    print(operations)
    hospitalname=request.GET['HospitalName']
    contact=request.GET['Phoneno']   
    email=request.GET['email']
    password=request.GET['Password']
   # department=request.GET['department']
    branchaddress=request.GET['Branchaddress']
    design=request.GET['design']
    #doctor=request.GET['doctor']
    r=Register.objects.get(email=email)
   
    if operations=="update":
        r.contact=contact
        r.hospitalname=hospitalname
        r.email=email
        r.branchaddress=branchaddress    
        r.password=password
        r.design=design
        r.save()

    else:
      #  email=request.GET['Mail']  
      #  r=Register.objects.get(email=email) 
        Register.delete(r)     


    user=Register.objects.all()
    return render(request,"viewuser.html",{"user":user})