from django.shortcuts import render
from acapp.form import UserForm, Memberform, PostblogForm
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'acapp/index.html')

@login_required        
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        member_form = Memberform(data=request.POST)

        if user_form.is_valid() and member_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            member = member_form.save(commit=False)
            member.user = user
            member.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        member_form = Memberform()

    return render(request, 'acapp/register.html',
                  {'user_form': user_form,
                   'member_form': member_form,
                   'registered': registered})


def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate (username=username,password = password)
        
        if user :
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('你沒有註冊')
        else:
            print('有人想盜帳號')
            print("帳號 {} and 密碼 {}".format(username,password))
            return HttpResponse('錯誤的帳號密碼')
    else:
        return render(request,'acapp/login.html',{})
        
def postblog(request):
    if request.method == 'POST':
        postblog_form = PostblogForm(data=request.POST)
        if postblog_form.is_valid():
            postblog = postblog_form.save()
            postblog.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        postblog_form = PostblogForm()
    return render(request,'acapp/postblog.html',{'postblogform':postblog_form})