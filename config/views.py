from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,logout
from django.contrib.auth  import authenticate,login as auth_login,logout
from Cards.models import *

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from Accounts.models import *

import random
import string

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here

def home(request):
    context={
        'banner':Banner.objects.all().last(),
        'client_logo':ClientLogo.objects.all(),
        'websitelogo':WebSiteLogo.objects.all().last(),
        'about':About.objects.all().last(),
        'service':Services.objects.all(),
        'features':Features.objects.all(),

        'why_choose_us':WhyChooseUs.objects.all(),
        'price':Pricing.objects.all().order_by('id'),
        'video':Video_section.objects.all().last(),

        'contact_heading':ContactHeading.objects.all().last(),
        'footer': Footer.objects.all().last(),

        'Why_Choose_Us_heading':Heading.objects.filter(heading_type="Why_Choose_Us").last(),
        'price_heading':Heading.objects.filter(heading_type="Price").last(),
        'about_heading':Heading.objects.filter(heading_type="About").last(),
        'service_heading':Heading.objects.filter(heading_type="Services").last(),
        'feature_heading':Heading.objects.filter(heading_type="Features").last(),
    }
    return render(request,"demo21.html",context)


def AboutPageview(request):
    context = {
        'banner':Banner.objects.all().last(),
        'client_logo':ClientLogo.objects.all(),
        'websitelogo':WebSiteLogo.objects.all().last(),
        'about':About.objects.all().last(),
        'service':Services.objects.all(),
        'features':Features.objects.all(),

        'why_choose_us':WhyChooseUs.objects.all(),
        'price':Pricing.objects.all(),
        'video':Video_section.objects.all().last(),

        'contact_heading':ContactHeading.objects.all().last(),
        'footer': Footer.objects.all().last(),

        'Why_Choose_Us_heading':Heading.objects.filter(heading_type="Why_Choose_Us").last(),
        'price_heading':Heading.objects.filter(heading_type="Price").last(),
        'about_heading':Heading.objects.filter(heading_type="About").last(),
        'service_heading':Heading.objects.filter(heading_type="Services").last(),
        'feature_heading':Heading.objects.filter(heading_type="Features").last(),
    }
    return render(request,"about.html",context)


def ContactUsPageview(request):
    context = {
        'banner':Banner.objects.all().last(),
        'client_logo':ClientLogo.objects.all(),
        'websitelogo':WebSiteLogo.objects.all().last(),
        'about':About.objects.all().last(),
        'service':Services.objects.all(),
        'features':Features.objects.all(),

        'why_choose_us':WhyChooseUs.objects.all(),
        'price':Pricing.objects.all(),
        'video':Video_section.objects.all().last(),

        'contact_heading':ContactHeading.objects.all().last(),
        'footer': Footer.objects.all().last(),

        'Why_Choose_Us_heading':Heading.objects.filter(heading_type="Why_Choose_Us").last(),
        'price_heading':Heading.objects.filter(heading_type="Price").last(),
        'about_heading':Heading.objects.filter(heading_type="About").last(),
        'service_heading':Heading.objects.filter(heading_type="Services").last(),
        'feature_heading':Heading.objects.filter(heading_type="Features").last(),
    }
    return render(request,"contact.html",context)


def post_contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not email or not message:
            data = {'msg': "Please fill out all fields", 'color_class': 'error-toast'}
            return JsonResponse(data, safe=False)
        elif Send_Contact.objects.filter(email=email):
            data={'msg':"Email is alredy exists", 'color_class': 'error-toast'}
            return JsonResponse(data,safe=False)
        else:
            new_contact=Send_Contact(name=name,email=email,message=message)
            new_contact.save()
            data={'msg':"Successfully contact send",'color_class':'success-toast'}
            return JsonResponse(data,safe=False)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def Signup(request):
    if request.method=="POST":
        full_name=request.POST['name']
        password=request.POST['password']
        email=request.POST['email']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                data={'msg':"Email already exists.", 'color_class': 'error-toast'}
                return JsonResponse(data, safe=False)
            else:
                user=User.objects.create(full_name=full_name,email=email,username=email,password=password)
                user.set_password(password)
                user.save()

                ctx = {'name':full_name}

                sub = 'Welcome to BusinessCard4U Platform'

                html_template = 'email/register.html'

                html_message = render_to_string(html_template, ctx)

                message = EmailMessage(sub, html_message, settings.EMAIL_HOST_USER, [request.POST.get('email')])
                message.content_subtype = 'html'  # this is required because there is no plain text email message
                message.send()

                data = {'msg':'Successfully Submitted.','color_class':'success-toast'}
                return JsonResponse(data, safe=False)
        else:
            data={'msg':"Password do not match", 'color_class': 'error-toast'}
            return JsonResponse(data, safe=False)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def Signin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request, username=email,password=password)
        if user is not None:
            auth_login(request,user)
            # return redirect('home')
            data = {'msg':'Successfully login.','color_class':'success-toast','redirect_url': reverse('mycard')}
            return JsonResponse(data, safe=False)
            # user = request.user
            # response_text = f"Hello {user.username}! Your email is {user.email}."
            # return HttpResponse(response_text)
        else:
            data={'msg':"Invalid credentials",'color_class': 'error-toast'}
            return JsonResponse(data, safe=False)

   
def Signout(request):
    logout(request)
    return redirect('home')

#--------------- otp varification work ----------------------

def OTPVarification(request):
    if request.method == 'POST':
        try:
            get_otp = request.POST.get('otp')
            get_otp_user = OTPS.objects.filter(user = request.user ,otp = get_otp).last()
            if get_otp_user:
                get_user = User.objects.get(username = request.user)
                get_user.card_access = True
                get_user.save()
                return redirect('mycard')
            #msg otp not valid please resend or enter again
            return redirect('mycard')
        except:
            #msg - please try again
            return redirect('mycard')



# def Table_view(request):
#     company_data=Forms_Model.objects.all().order_by('-id')
#     return render(request,"table.html",{'company_data':company_data,})

#
# def Index(request,slug):
#     company_detail=Forms_Model.objects.get(slug=slug)
#     print(company_detail.id)
#     company_id = company_detail.id
#     pro_img = Product_Image.objects.filter(my_model=company_id)
#     gallery_image = Gallery_Image.objects.filter(my_model=company_id)
#     return render(request,"index.html",{'company_detail':company_detail,'pro_img':pro_img,'gallery_image':gallery_image})


def Post_enquiry(request):
    try:
        if request.method=="POST":
            name = request.POST.get('name', '').strip()
            mobile = request.POST.get('mobile', '').strip()
            message = request.POST.get('message', '').strip()
            card_id = request.POST.get('card_id', '').strip()

            if not name or not mobile or not message:
                data = {'msg': "Please fill out all fields", 'color_class': 'error-toast'}
                return JsonResponse(data, safe=False)
            elif Enquiry.objects.filter(mobile=mobile):
                data={'msg':"Mobile number is already exists", 'color_class': 'error-toast'}
                return JsonResponse(data,safe=False)
            else:
                get_card = Cards.objects.filter(id = card_id).last()
                new_enquiry=Enquiry(card_id = get_card,name=name,mobile=mobile,message=message)
                new_enquiry.save()
                data={'msg':"Successfully enquiry send",'color_class':'success-toast'}
                return JsonResponse(data,safe=False)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    except Exception as e:
        data = {'msg': "Somethig worng please try again", 'color_class': 'error-toast'}
        return JsonResponse(data, safe=False)



def SubscribeView(request):
    try:
        if request.method=="POST":
            email = request.POST.get('email', '').strip()
            if not email:
                data = {'msg': "Please fill out all fields", 'color_class': 'error-toast'}
                return JsonResponse(data, safe=False)
            elif Subscribe.objects.filter(email=email):
                data={'msg':"Email is already exists", 'color_class': 'error-toast'}
                return JsonResponse(data,safe=False)
            else:
                new_enquiry=Subscribe(email = email)
                new_enquiry.save()
                data={'msg':"Successfully Subscribed",'color_class':'success-toast'}
                return JsonResponse(data,safe=False)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    except Exception as e:
        data = {'msg': "Somethig worng please try again", 'color_class': 'error-toast'}
        return JsonResponse(data, safe=False)



def ForgetPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        get_email = User.objects.filter(email = email).last()

        if get_email:
            length = 10
            # Define the possible characters for the alphanumeric number
            characters = string.ascii_uppercase + string.digits
            # Generate the random alphanumeric number
            alphanumeric = ''.join(random.choice(characters) for i in range(length))

            get_email.set_password(alphanumeric)
            get_email.save()

            ctx = {'username': get_email.username,'pass': alphanumeric}

            sub = 'Welcome to BusinessCard4U Platform'

            html_template = 'email/forget_pass_email.html'

            html_message = render_to_string(html_template, ctx)

            message = EmailMessage(sub, html_message, settings.EMAIL_HOST_USER, [get_email.email])
            message.content_subtype = 'html'  # this is required because there is no plain text email message
            message.send()

            data = {'msg':"Successfuly foreget Password Please check your email",'color_class': 'success-toast'}
            return JsonResponse(data, safe=False)

        data = {'msg':"Email is not matched" ,'color_class':'error-toast'}
        return JsonResponse(data,safe=False)



def StaticPageView(request,id):
    get_page = StaticPage.objects.filter(slug = id).last()

    if not get_page:
        return redirect('home')

    ctx = {
        'websitelogo': WebSiteLogo.objects.all().last(),
        'footer': Footer.objects.all().last(),
        'get_page':get_page,
    }
    return render(request,'static_page.html',ctx)

