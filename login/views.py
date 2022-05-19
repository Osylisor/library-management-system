from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User

def login_user(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user_to_login =  authenticate(request, email = email, password = password)

        if user_to_login is not None:
            messages.success(request, 'Login successful, welcom to LMS.')
            login(request, user_to_login)
            return redirect('home')
        else:
            messages.error(request, 'The password or the email is invalid.')
            return redirect('/')


    return render(request, 'login/login.html', {})


def register(request):
     return render(request, 'login/register.html', {})


def register_student(request):

    if request.method == 'POST':

        #Get the form data
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        student_number = request.POST.get('student_number')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        #Check if there is a user with this email
        if User.objects.filter(email = email).exists():
            messages.error(request, 'This email is taken')
            return redirect('student_register')

        #Check if there is a user with this student number
        if(User.objects.filter(student_number = student_number).exists()):
            messages.error(request, 'The student number is taken')
            return redirect('student_register')


          #Check if the name and surname fields are at least 3 characters long
        if len(name) < 2 or len(surname) < 2:
            messages.error(request, 
            'Both the name and the surname field have to be at least 3 characters long')
            return redirect('student_register')


        #Check if the student number is at least 9 characters long
        if len(student_number) < 9:
            messages.error(request, 
            'The student number should be at least 9 characters long')
            return redirect('student_register')

        #Check if the email address is too short
        if len(email) < 6:
            messages.error(request, "The email address you've provided is too short")
            return redirect('student_register')


        #Check if the password is 8 or more characters long
        if len(password1) < 8:
            messages.error(request, 'The password should be at least 8 characters long')
            return redirect('student_register')


        #Check if the passwords match
        if password1 == password2:

        

            user = User.objects.create_user(email = email, name = name + " " + surname, 
            password = password1)
            user.student_number = student_number
            user.save()
            messages.success(request, 'Account Created!')
            login(request, user)
            return redirect('home')
        else:

            messages.error(request,"The password doesn't match.")
            return redirect('student_register')

    return render(request, 'login/student register.html', {})

#continue by fixing the registration bugs, then proceed to the main application.

def register_admin(request):


    if request.method == 'POST':

        #Get the form data
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        #Check if there is a user with this email
        if User.objects.filter(email = email).exists():
            messages.error(request, 'This email is taken')
            return redirect('admin_register')

        #Check if the name and surname fields are at least 3 characters long
        if len(name) < 2 or len(surname) < 2:
            messages.error(request, 
            'Both the name and the surname field have to be at least 3 characters long')
            return redirect('admin_register')

        
        #Check if the email address is too short
        if len(email) < 6:
            messages.error(request, "The email address you've provided is too short")
            return redirect('admin_register')

        #Check if the password is 8 or more characters long
        if len(password1) < 8:
            messages.error(request, 'The password should be at least 8 characters long')
            return redirect('admin_register')

        #Check if the passwords match
        if password1 == password2:

            user = User.objects.create_admin_user(email = email, name = name + " " + surname, 
            password = password1)
            user.save()
            messages.success(request, 'Account Created!')
            login(request, user)
            return redirect('home')
        else:

            messages.error(request,"The password doesn't match.")
            return redirect('admin_register')

    return render(request, 'login/admin register.html', {})
