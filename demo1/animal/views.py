from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login as lgi,logout as lgo
from animal.models import Article,Classify,Comment,Label,Album,Img
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings
# Create your views here.

def index(request):
    articles=Article.objects.all()
    indeximgs = Album.objects.all()

    return render(request,'index.html',locals())

def single(request,id):
    article = Article.objects.get(pk=id)
    articles = Article.objects.all()
    class_i=Classify.objects.all()
    tags=Label.objects.all()
    date = Article.objects.dates('create_time', 'month', order='DESC')
    return render(request,'single.html',locals())

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=username,password=pwd)

        if user:
            lgi(request,user)

            return redirect(reverse('animal:index'))
        else:
            return render(request,'index.html',)

def logout(request):
    res=redirect(reverse('animal:index'))
    lgo(request)
    return res

def register(request):
    if request.method == 'POST':
        username=request.POST.get('regis_name')
        email=request.POST.get('email')
        pwd=request.POST.get('password_1')
        pwd1=request.POST.get('password_2')

        if pwd != pwd1:
            errors='密码不一致'
            return render(request,'index.html',{'errors':errors})
        else:
            user=User.objects.create_user(username=username,password=pwd,email=email)
            user.save()
            return render(request,'index.html')

def comment(request,id):
    if request.method=='GET':
        return render(request, 'single.html')
    elif request.method == 'POST':
        b = Article.objects.get(pk=id)
        com=Comment()
        com.name=request.POST.get('Name')
        com.email=request.POST.get('Email')
        com.message=request.POST.get('Message')
        com.article=b
        com.save()
        return HttpResponseRedirect('/animal/single/%s/'%(id))


def classify(request,id):
    articles=get_object_or_404(Classify, pk=id).article_set.all()
    return render(request, 'index.html', locals())


def recent(request,id):
    articles =Article.objects.all().order_by('-create_time')
    article = Article.objects.get(pk=id)
    class_i = Classify.objects.all()
    tags = Label.objects.all()
    return render(request, 'single.html',locals())

def file(request,year,month):
    articles =Article.objects.filter(create_time__year=year,create_time__month=month)
    return render(request, 'index.html', locals())

def label(request,id):
    articles = get_object_or_404(Label, pk=id).article_set.all()
    return render(request,'index.html',locals())


def indeximg(request):
    return render(request,'index,html',locals())

def gallery(request):
    img=Img.objects.all()
    return render(request, 'gallery.html', locals())

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def typography(request):
    return render(request,'typo.html')

def icons(request):
    return render(request,'icons.html')

class Contacts(View):

    def get(self,request):
        return render(request,'contact.html',locals())
    def post(self,request):
        try:
            send_mail('欢迎来到宠物之家', '欢迎来到宠物之家', settings.DEFAULT_FROM_EMAIL, ["1327870569@qq.com"])
        except Exception as e:
            print(e)

        return render(request,'contact.html',{'info':'成功',})