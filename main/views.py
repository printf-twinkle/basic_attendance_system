from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as dj_login

from main.models import User

 

def teacher_register(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        password = make_password(request.POST["password1"])
        print(name, email, password)
        try:
            if not User.objects.filter(email=email).exists():
                user = User.objects.create(
                    name=name,
                    email=email,
                    password=password,
                    is_teacher=True
                )
                user.save()
                messages.success(
                    request, " Your account has been successfully created")
                return redirect("home")
            elif User.objects.filter(email=email).exists():
                messages.error(
                    request, " User already exists!!!Try logging in")
                return redirect("teacher_register")
        except Exception as e:
            print(e)
    return render(request, "main/teacher_register.html")

 

def student_register(request):
    if request.method == 'POST':
        if request.user.is_admin:
            name = request.POST["name"]
            roll_number = request.POST["roll_number"]
            email = request.POST["email"]
            password = make_password(request.POST["password1"])
            print( email, password)
            try:
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create(
                        email=email,
                        name=name,
                        roll_number=roll_number,
                        password=password,
                        is_student=True
                    )
                    user.save()
                    messages.success(
                        request, " Your account has been successfully created")
                    return redirect("home")
                elif User.objects.filter(email=email).exists():
                    messages.error(
                        request, " User already exists!!!Try logging in")
                    return redirect("student_register")
            except Exception as e:
                print(e)
        elif request.user.is_authenticated and not request.user.is_admin:
            messages.error(
                        request, " Only an admin can create an account!")
            return redirect("student_register")
    return render(request, "main/student_register.html")
 


def student_login(request):
    if request.user.is_authenticated == True:
        return redirect("home")
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, password)
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            dj_login(request, user)
            # print(request.user.id/is_authenticated)
            messages.success(request, " Successfully logged in")
            return redirect("home")
        else:
            messages.error(request, " Invalid Credentials, Please try again")
    return render(request, "main/student_login.html")
 

def teacher_login(request):
    if request.user.is_authenticated == True:
        return redirect("home")
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, password)
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            dj_login(request, user)
            # print(request.user.id/is_authenticated)
            messages.success(request, " Successfully logged in")
            return redirect("home")
        else:
            messages.error(request, " Invalid Credentials, Please try again")
    return render(request, "main/teacher_login.html")

 


def admin_login(request):
    if request.user.is_authenticated == True:
        return redirect("home")
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, password)
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            print("ii")
            dj_login(request, user)
            print("yes")
            messages.success(request, " Successfully logged in")
            print("okay")
            return redirect("home")
        else:
            messages.error(request, " Invalid Credentials, Please try again")
    return render(request, "main/admin_login.html")
 


def home(request):
    context = {}
    request_status = []
    all_user_objects = User.objects.all()
    if request.user.is_authenticated and request.user.is_teacher:
        print("teacher")
        context['users'] = all_user_objects
         
    elif request.user.is_authenticated and request.user.is_admin:
        print("admin")
        context['users'] = all_user_objects
        context['count'] = len(all_user_objects)
    elif request.user.is_authenticated and request.user.is_student:
        print("student")
        context['user_id'] = request.user
    else:
        return render(request, "main/index.html")
    return render(request, 'main/home.html', context=context)
 
def give_attendance(request, user_id):
    get_user = User.objects.get(email=user_id)
    get_user.is_present = True
    get_user.save()
    return redirect("home")

def request_attendance(request, user_id):
    get_user = User.objects.get(email=user_id)
    get_user.is_request = True
    get_user.save()
    return redirect("home")

def handlelogout(request):
    logout(request)
    messages.success(request, " Successfully logged out")
    return render(request, "main/index.html")