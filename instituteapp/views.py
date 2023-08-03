from django.shortcuts import render,redirect
from .models import Courses
from .models import contactData,FeedbackData
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout
import datetime as dt
data1=dt.datetime.now()
from django.contrib import messages
from django.http import HttpResponseRedirect


#@login_required(login_url='login')
def homePage(request):
    return render(request,'homePage.html')

#@login_required(login_url='login')
def contactPage(request):
    if request.method=='GET':
        data= contactData.objects.all()
        return render(request,'contactPage.html')
    else:
         contactData(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            mobile = request.POST['mobile'],
            location= request.POST['location']
                ).save()
    return redirect(contactPage)

def servicePage(request):
    courses=Courses.objects.all()
    return render(request,'servicePage.html', {'courses':courses})

def feedbackPage(request):
    if request.method=='GET':
        feedbacks=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedbackPage.html',{'feedbacks':feedbacks})
    else:
        FeedbackData(
        content=request.POST['feedback'],
        date=data1
        ).save()
        feedbacks=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedbackPage.html',{'feedbacks':feedbacks})


def galleryPage(request):
    return render(request,'galleryPage.html')

def reg_Page(request):
    if request.method=='GET':
        form =RegistrationForm()
        return render(request,'registerPage.html',{'form':form})
    else:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user=user.set_password(user.password)
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid details. Please check your inputs.')
    return render(request, 'registerPage.html', {'form': form})


def login_Page(request):
    if request.method=='GET':
        return render(request,'loginPage.html')
    else:
        user=request.POST['user']
        password=request.POST['password']
        user=authenticate(username=user,password=password)
        if user is not None:
            login(request,user)
            # messages.success(request, "Login successful. Welcome to our website!")
            return HttpResponseRedirect('home')
        else:
            messages.error(request, "Invalid login details. Please try again.")
            return HttpResponseRedirect('login')

def logout_Page(request):
    logout(request)
    messages.success(request, "Logout successful.", extra_tags='alert-success')
    return redirect('login')