from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersform
from myapp.models import Service
from news.models import News
from saveenquiry.models import saveenquiry
from django.core.paginator import Paginator 
#from django.core.mail import send_mail,EmailMultiAlternatives


def HomePage(request):
   # subject='Testing Mail'
   # from_email='figmajacell@gmail.com'
   # msg='<p>Welcome to <b>MYPROJECT</b></p>'
   # to='jacelljamble@gmail.com'
   # msg=EmailMultiAlternatives(subject,msg,from_email,[to])
   # msg.content_subtype='html'
   # msg.send()
    
   # send_mail(
   # 'Testing Mail',
   # 'Hello Jacell Jamble Here',
   # 'figmajacell@gmail.com',  # Sender email
   # ['jacelljamble@gmail.com'],  # Recipient email
   # fail_silently=False,
   # )
    newsData=News.objects.all();
    servicesData=Service.objects.all().order_by('service_title')[:3]
    
    data={
       # 'title':'Home New',
       # 'bdata':'Welcome to myproject',
       # 'clist':['PHP','Java','Django'],
       # 'numbers':[10,20,30,40,50],
       # 'student_details':[
       #     {'name':'pradeep','phone':9675794759},
       #     {'name':'testing','phone':9833823888}
       # ]
       
       'servicesData':servicesData,
       'newsData':newsData
    }
    return render(request,"homepage.html",data)

def aboutUs(request):
    return HttpResponse("Welcome to aboutus")

def Course(request):
    return HttpResponse("Welcome to course")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def Login(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"login.html",{'output':output})

def userform(request):
    finalval=0
    fn=usersform()
    data={'form':fn}
    try:
        if request.method=="POST":
         n1=int(request.POST.get('num1'))
         n2=int(request.POST.get('num2'))
         finalval= n1+n2
         data={
            'form':fn,
            'output':finalval
         }
         
         url="/logineco/?output={}".format(finalval)
         
         return HttpResponseRedirect(url)
         
         # or we can use:
         # return HttpResponseRedirect('/logineco/')
         # for -> from django.http import HttpResponse,HttpResponseRedirect
         # use -> return HttpResponseRedirect('/logineco/')
         # for -> from django.shortcuts import render,redirect
         # use -> return redirect('/logineco/')
        
    except:
        pass
    return render(request,"userform.html",data)

def submitform(request):
    try:
        if request.method=="POST":
         n1=int(request.POST.get('num1'))
         n2=int(request.POST.get('num2'))
         finalval= n1+n2
         data={
            'n1':n1,
            'n2':n2,
            'output':finalval
         }
         
         return HttpResponse(finalval)
    except:
        pass 
        
def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2;
            elif opr=="-":
                c=n1-n2;
            elif opr=="*":
                c=n1*n2;
            elif opr=="/":
                c=n1/n2;
               
                
               
    except:
        c="Invalid opr......"
        
    print(c)
    
    return render(request,"calculator.html",{'c':c})


def evenodd(request):
    c=''
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request,"evenodd.html",{'error':True})
            
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Even Number"
        else:
            c="Odd Number"
           
    return render(request,"evenodd.html",{'c':c})


def marksheet(request):
    if request.method=="POST":
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))
        t=s1+s2+s3+s4+s5
        p=t*100/500;
        if p>=60:
            d="1st Div"
        elif p>=48:
            d="2nd Div"
        elif p>=35:
            d="3rd Div"
        else:
            d="Fail"
        data={
            'total':t,
            'per':p,
            'div':d,
        }
        return render(request,"marksheet.html",data)
        
    return render(request,"marksheet.html")


def services(request):
    servicesData=Service.objects.all().order_by('service_title')
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            servicesData=Service.objects.filter(service_title__icontains=st)
    
    paginator=Paginator(servicesData,2)
    page_number=request.GET.get('page')
    servicesDatafinal=paginator.get_page(page_number)
    totalpage=servicesDatafinal.paginator.num_pages
          
    data={
        
       #'servicesData':servicesData
        'servicesData':servicesDatafinal,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)] 
    }
    return render(request,"services.html",data)


def newsdetails(request,slug):
    newsdetails=News.objects.get(news_slug=slug)
   
    data={
     
       'newsdetails':newsdetails
    }
    return render(request,"newsdetails.html",data)

def saveEnquiry(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        website=request.POST.get('website')
        message=request.POST.get('message')
        en=saveenquiry(name=name,email=email,phone=phone,websiteLink=website,message=message)
        en.save()
        n='Data Inserted'
        
    
    return render(request,"saveenquiry.html",{'n':n})
    
