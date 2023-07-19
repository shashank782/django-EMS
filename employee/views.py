from django.shortcuts import render,redirect
from .models import *

from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as auth_login

# Create your views here.
def index(request):
    return render(request,'index.html')



def registration(request):
    error=""
    if request.method == "POST":
        F_name= request.POST['firstname']
        L_name= request.POST['lastname']
        E_number= request.POST['EmpNumber']
        Em= request.POST['Email ID']
        Pwd= request.POST['pwd']
        try:
            user= User.objects.create_user(first_name=F_name, last_name=L_name,username=Em, password=Pwd,)
            EmployeeDetail.objects.create(user= user, empNumber =E_number)
            EmployeeExperience.objects.create(user= user,)
            EmployeeEducation.objects.create(user= user,)
            error="no"
        except:
            error="yes"    
    return render(request,'registration.html',locals())


def login(request):
    error=""
    if request.method =='POST':
        E= request.POST['emailid']
        P= request.POST['password']
        user = authenticate(username=E,password=P)
        if user:
            auth_login(request,user)
            error="no"
        else:
            error="yes"          
   
    return render(request,'login.html',locals())



def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'home.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error =""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)

    if request.method == "POST":
        F_name= request.POST['firstname']
        L_name= request.POST['lastname']
        E_number= request.POST['EmpNumber']
        Dg= request.POST['Designation']
        De= request.POST['Department']
        
        co= request.POST['contact']
        joindate= request.POST['jdate']
        gend= request.POST['gender']
        


        employee.user.first_name = F_name # It allows to edit the name and show previous name
        employee.user.last_name = L_name
        employee.empNumber = E_number
        employee.designation = Dg
        employee.empDept = De # empDept model variable hai do not get confuse
        employee.contact = co
        employee.gender = gend

        if joindate:
            employee.joiningDate =joindate




        try:
            employee.save() # emplyee model fields will update
            employee.user.save() # for foreignkey values update
            error="no"
        except:
            error="yes"    
    return render(request,'profile.html',locals())
    


def Logout(request):
    logout(request) #destroy the session
    return redirect('index')











def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    
    return render(request,'my_experience.html',locals())



def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error =""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    if request.method == "POST":
        company1name= request.POST['company1name']
        company1desig= request.POST['company1desig']
        company1salary= request.POST['company1salary']
        company1duration= request.POST['company1duration']
        
        company2name= request.POST['company2name']
        company2desig= request.POST['company2desig']
        company2salary= request.POST['company2salary']
        company2duration= request.POST['company2duration']
        
        company3name= request.POST['company3name']
        company3desig= request.POST['company3desig']
        company3salary= request.POST['company3salary']
        company3duration= request.POST['company3duration']
        


        experience.company1name = company1name # It allows to edit the name and show previous name
        experience.company1desig = company1desig
        experience.company1salary =company1salary
        experience.company1duration =company1duration
        
        experience.company2name = company2name # It allows to edit the name and show previous name
        experience.company2desig = company2desig
        experience.company2salary =company2salary
        experience.company2duration =company2duration
        
        experience.company3name = company3name # It allows to edit the name and show previous name
        experience.company3desig = company3desig
        experience.company3salary =company3salary
        experience.company3duration =company3duration

       
        try:
            experience.save()            
            error="no"
        except:
            error="yes"    
    return render(request,'edit_experience.html',locals())





def my_education(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    education = EmployeeEducation.objects.get(user=user)   
    return render(request,'my_education.html',locals())










def edit_education(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error =""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)

    if request.method == "POST":
        courseug= request.POST['courseug']
        schoolclgug= request.POST['schoolclgug']
        yearofpassingug= request.POST['yearofpassingug']
        percentageug= request.POST['percentageug']
        
        coursepg = request.POST['  coursepg ']
        schoolclgpg= request.POST['schoolclgpg']
        yearofpassingpg= request.POST['yearofpassingpg']
        percentagepg= request.POST['percentagepg']
        
        coursessc= request.POST['coursessc']
        schoolclgssc= request.POST['schoolclgssc']
        yearofpassingssc= request.POST['yearofpassingssc']
        percentagessc= request.POST['percentagessc']

        coursehsc= request.POST['coursehsc']
        schoolclghsc= request.POST['schoolclghsc']
        yearofpassinghsc= request.POST['yearofpassinghsc']
        percentagehsc= request.POST['percentagehsc']
        


        education.courseug = courseug # It allows to edit the name and show previous name
        education.schoolclgug = schoolclgug
        education.yearofpassingug=yearofpassingug
        education.percentageug =percentageug

        education.coursepg = coursepg # It allows to edit the name and show previous name
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg=yearofpassingpg
        education.percentagepg =percentagepg
        
        education.coursessc = coursessc # It allows to edit the name and show previous name
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc =yearofpassingssc
        education.percentagessc =percentagessc
        
        education.coursehsc = coursehsc # It allows to edit the name and show previous name
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc =yearofpassinghsc
        education.percentagehsc =percentagehsc
        
       

       
        try:
            education.save()            
            error="no"
        except:
            error="yes"    
    return render(request,'edit_education.html',locals())






def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error =""
    user = request.user
    
    if request.method == "POST":
        curr_pass =request.POST['currentpassword']
        new_pass = request.POST['newpassword']        
       
        try:
            if user.check_password(curr_pass):  # check password is given by django
               user.set_password(new_pass)
               user.save()      
               error="no"
            else:
                error="not"   
        except:
            error="yes"    
    return render(request,'change_password.html',locals())

'''def admin_login(request):
    error=""
    if request.method =='POST':
        userrr= request.POST['username']
        pa= request.POST['pwd']
        user = authenticate(username=userrr,password=pa)
        if user.is_staff:
            auth_login(request,user)
            error="no"
        else:
            error="yes"          
   
    return render(request,'admin_login.html',locals())



def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_login.html')'''