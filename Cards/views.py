from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,logout
from django.contrib.auth  import authenticate,login as auth_login,logout
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from config.checksum import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from config.models import *


import random
import string


from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.utils.text import slugify
from .communications import *

from django.shortcuts import redirect
import base64
import json

#----------------------- start working ------------------------------------

@login_required
def CreateCard(request):
    get_config = Config.objects.all().last()

    if not get_config:
        day = 30
    else:
        day = get_config.card_expiry_days

    now_datetime = datetime.now()
    ex_date = now_datetime + timedelta(days=day)

    card = Cards()
    card.user = request.user
    card.expiry_date = ex_date
    card.save()
    return redirect('add_company_info',card.id)


@login_required
def AddComInfoView(request,pk):
    card = Cards.objects.get(id = pk)
    get_cominfo = ComInfo.objects.filter(card_id = card).last()

    if get_cominfo:
        form = ComInfoForms(request.POST or None,request.FILES or None,instance = get_cominfo)
    else:
        form = ComInfoForms(request.POST or None,request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit = False)
            f.card_id = card
            f.save()

            #----------- slug generate -------------------------------------

            base_slug = slugify(request.POST.get('company_name'))[:5]
            counter = 1
            generated_slug = base_slug
            while Cards.objects.filter(slug=generated_slug).exists():
                counter_str = str(counter)
                if len(counter_str) + len(base_slug) > 8:
                    # Not enough space to append the counter, truncate the base_slug
                    base_slug = base_slug[:4 - len(counter_str)]
                generated_slug = f"{base_slug}{counter_str}"
                counter += 1

            card.slug = generated_slug
            card.save()

            #--------------- end slug work ----------------------


            #--------------- checking for after payment country change or not --------------------
            if get_cominfo:
                if card.payment_status == True:
                    if card.currency == 'inr':
                        if request.POST.get('country') == 'India':
                            f.state = request.POST.get('state')
                            f.city = request.POST.get('city')
                            f.save()
                        else:
                            pass
                    elif card.currency == 'usd':
                        f.country = request.POST.get('country')
                        f.state = request.POST.get('state')
                        f.city = request.POST.get('city')
                        f.save()
                else:
                    pass
            else:
                f.country = request.POST.get('country')
                f.state = request.POST.get('state')
                f.city = request.POST.get('city')
                f.save()

            return redirect('add_social_video',card.id)

    ctx = {
        'form':form,
        'card':card,
        'get_cominfo':get_cominfo,
        'footer': Footer.objects.all().last(),
        'websitelogo': WebSiteLogo.objects.all().last(),
    }
    return render(request,'cards/com_info.html',ctx)


@login_required
def AddSocialView(request,pk):
    card = Cards.objects.get(id = pk)
    get_social = Social.objects.filter(card_id=card).last()

    if get_social:
        form = SocialForms(request.POST or None, request.FILES or None, instance = get_social)
    else:
        form = SocialForms(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit = False)
            f.card_id = card
            f.save()
            return redirect('add_about',card.id)

    ctx = {
        'form':form,
        'card':card,
        'footer': Footer.objects.all().last(),
        'websitelogo': WebSiteLogo.objects.all().last(),
    }
    return render(request,'cards/social_video.html',ctx)


@login_required
def AddAboutInfoView(request,pk):
    card = Cards.objects.get(id = pk)
    get_about = AboutInfo.objects.filter(card_id=card).last()

    if get_about:
        form = AboutInfoForms(request.POST or None, request.FILES or None, instance = get_about)
    else:
        form = AboutInfoForms(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit = False)
            f.card_id = card
            f.save()
            return redirect('add_product_and_service',card.id ,'id')

    ctx = {
        'form':form,
        'card':card,
        'footer': Footer.objects.all().last(),
        'websitelogo': WebSiteLogo.objects.all().last(),
    }
    return render(request,'cards/about.html',ctx)


@login_required
def BankDetailView(request,pk):
    card = Cards.objects.get(id = pk)
    get_bank = BankDetail.objects.filter(card_id=card).last()

    if get_bank:
        form = BankDetailForms(request.POST or None, request.FILES or None, instance = get_bank)
    else:
        form = BankDetailForms(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit = False)
            f.card_id = card
            f.save()
            return redirect('add_gallery',card.id , 'id')

    ctx = {
        'form':form,
        'card':card,
        'footer': Footer.objects.all().last(),
        'websitelogo': WebSiteLogo.objects.all().last(),
    }
    return render(request,'cards/bank_details.html',ctx)


@login_required
def ProductServiceView(request,pk,id=None):
    card = Cards.objects.get(id = pk)
    get_ps = None

    try:
        get_ps = ProductAndService.objects.filter(id = id).last()
    except:
        pass

    if get_ps:
        form = ProductAndServiceForms(request.POST or None, request.FILES or None, instance = get_ps)
        get_ps = get_ps.id
    else:
        form = ProductAndServiceForms(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit = False)
            f.card_id = card
            f.save()
            return redirect('add_product_and_service',card.id ,'id')

    ctx = {
        'form':form,
        'card':card,
        'get_ps':get_ps,
        'ps':ProductAndService.objects.filter(card_id = card),
        'ps_count':ProductAndService.objects.filter(card_id = card).count(),
        'footer': Footer.objects.all().last(),
        'websitelogo': WebSiteLogo.objects.all().last(),
        'config': Config.objects.all().last(),
    }
    return render(request,'cards/product_service.html',ctx)


@login_required
def ProductServiceDeleteView(request,pk,id=None):
    card = Cards.objects.get(id = pk)

    try:
        get_ps = ProductAndService.objects.filter(id = id).last()
        get_ps.delete()
        return redirect('add_product_and_service', card.id, 'id')
    except:
        return redirect('add_product_and_service', card.id, 'id')


@login_required
def GalleryView(request,pk,id=None):
    card = Cards.objects.get(id = pk)
    get_ps = None

    try:
        get_ps = Gallery.objects.filter(id = id).last()
    except:
        pass

    if get_ps:
        form = GalleryForms(request.POST or None, request.FILES or None, instance = get_ps)
        get_ps = get_ps.id
    else:
        form = GalleryForms(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit = False)
            f.card_id = card
            f.save()
            return redirect('add_gallery',card.id , 'id')

    ctx = {
        'form':form,
        'card':card,
        'get_ps':get_ps,
        'ps':Gallery.objects.filter(card_id = card),
        'ps_count':Gallery.objects.filter(card_id = card).count(),
        'footer': Footer.objects.all().last(),
        'websitelogo': WebSiteLogo.objects.all().last(),
        'config': Config.objects.all().last(),
    }
    return render(request,'cards/gallery.html',ctx)


@login_required
def GaleryDeleteView(request,pk,id=None):
    card = Cards.objects.get(id = pk)
    try:
        get_ps = Gallery.objects.filter(id = id).last()
        get_ps.delete()
        return redirect('add_gallery',card.id , 'id')
    except:
        return redirect('add_gallery',card.id , 'id')



@login_required
def SettingView(request,pk):
    card = Cards.objects.get(id = pk)
    get_setting = Setting.objects.filter(card_id=card).last()

    if get_setting:
        form = SettingForms(request.POST or None, request.FILES or None, instance = get_setting)
    else:
        form = SettingForms(request.POST or None, request.FILES or None)

    try:
        get_bg_image = TemplateBackgroundImage.objects.filter(id=request.POST.get('template_bg_image')).last()
    except:
        get_bg_image = None

    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit = False)
            f.card_id = card
            f.color = request.POST.get('color_code_s')
            f.font_color = request.POST.get('font_color_s')
            f.primary_font = request.POST.get('primary_font_s')
            f.secondry_font = request.POST.get('secondry_font_s')
            f.bg_image = get_bg_image
            f.save()
            return redirect('mycard')

    ctx = {
        'card':card,
        'form':form,
        'setting':get_setting,
        'cominfo':ComInfo.objects.filter(card_id = card).last(),
        'social':Social.objects.filter(card_id = card).last(),
        'about':AboutInfo.objects.filter(card_id = card).last(),
        'productandservice':ProductAndService.objects.filter(card_id = card),
        'bankdetail':BankDetail.objects.filter(card_id = card).last(),
        'gallery':Gallery.objects.filter(card_id = card),
        'footer': Footer.objects.all().last(),
        'websitelogo': WebSiteLogo.objects.all().last(),
        'bg_image': TemplateBackgroundImage.objects.all(),
    }
    return render(request,'cards/setting.html',ctx)


@login_required
def MyDashboard(request):
    card = Cards.objects.filter(user = request.user,is_delete = False).order_by('-id')
    # Pricing = Pricing.objects.all()

    ctx = {
        'card':card,
        # 'pricing':pricing,
        'footer':Footer.objects.all().last(),
        'websitelogo': WebSiteLogo.objects.all().last()
    }
    return render(request,'cards/dashboard.html',ctx)


def CardTemplateView(request,slug):
    card = Cards.objects.filter(slug = slug).last()


    if not card:
        return redirect('home')
    else:
        get_setting = Setting.objects.filter(card_id=card).last()
        if not get_setting:
            return redirect('home')

    if card.active_deactive == False:
        return redirect('home')

    try:
        now_datetime = datetime.now()
        if card.expiry_date.strftime('%Y-%m-%d') <= now_datetime.strftime('%Y-%m-%d'):
            return redirect('home')
    except:
        pass

    if not request.user.is_authenticated:
        card.views += 1
        card.save()

    ctx = {
        'card':card,
        'cominfo':ComInfo.objects.filter(card_id = card).last(),
        'social':Social.objects.filter(card_id = card).last(),
        'about':AboutInfo.objects.filter(card_id = card).last(),
        'productandservice':ProductAndService.objects.filter(card_id = card),
        'bankdetail':BankDetail.objects.filter(card_id = card).last(),
        'gallery':Gallery.objects.filter(card_id = card),
        'setting':Setting.objects.filter(card_id = card).last(),
        'websitelogo': WebSiteLogo.objects.all().last(),
        'footer': Footer.objects.all().last(),
    }
    return render(request,'cards/template_index.html',ctx)


#------------------------------------ card payment wokr -----------------------------------

from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from .models import *
from django.views.generic import ListView, CreateView, DetailView, TemplateView
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from django.urls import reverse, reverse_lazy

#----------------------------------------- start working ----------------------------

def CardPricing(request,pk):
    pricing = Pricing.objects.filter(plan_type = 'Individual')
    card = Cards.objects.get(id = pk)

    ctx = {
        'pricing':pricing,
        'card':card,
        'websitelogo': WebSiteLogo.objects.all().last(),
        'footer': Footer.objects.all().last(),
    }
    return render(request,'cards/pricing.html',ctx)



def CheckoutCart(request,card_id,price_id):
    card = Cards.objects.get(id=card_id)
    price = Pricing.objects.get(id=price_id)
    stripe_publishable_key = settings.STRIPE_PUBLIC_KEY

    get_com_info = ComInfo.objects.filter(card_id = card).last()

    amount = 0
    if get_com_info.country == 'India':
        amount = price.amounts_INR
        card.currency = 'inr'
        card.save()

        order = Orders()
        order.card_id = card
        order.price_id = price
        order.validity = price.validity
        order.amount = int(amount)
        order.save()

        order.features.add(*price.features.all())

        #------***************-------------------*******************

        url = str(request.scheme) + '://' + str(request.get_host() + '/pv-api/order/phonepe_callback/')
        # url1 = str('https://pvweb.greatfuturetechno.com/order-status/' + str(order.id))

        amount = int(order.amount * 100)

        payload = {
            "merchantId": "PGTESTPAYUAT78",
            "merchantTransactionId": str(order.id),
            "merchantUserId": str(request.user.username),
            "amount": amount,
            # "redirectUrl": str(url1),
            "redirectMode": "POST",
            "callbackUrl": str(url),
            "mobileNumber": str(get_com_info.contact_number_1),
            "paymentInstrument": {
                "type": "PAY_PAGE"
            }
        }

        url = CreatePhonePyChecksome(payload)
        return redirect(url)
    else:
        amount = price.amounts_USD
        card.currency = 'usd'
        card.save()

        order = Orders()
        order.card_id = card
        order.price_id = price
        order.validity = price.validity
        order.amount = int(amount)
        order.save()

        order.features.add(*price.features.all())

        ctx = {
            'order':order,
            'stripe_publishable_key':stripe_publishable_key
        }
        return render(request,'cards/payment.html',ctx)


@csrf_exempt
def create_checkout_session(request,id):
    request_data = json.loads(request.body)
    get_order = Orders.objects.filter(id = id).last()

    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        # Customer Email is optional,
        # It is not safe to accept email directly from the client side
        customer_email=request_data['email'],
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': str(get_order.card_id.currency),
                    'product_data': {
                        'name': get_order.card_id.slug,
                    },
                    'unit_amount': int(get_order.amount * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )

    get_order.stripe_payment_intent = checkout_session['payment_intent']
    get_order.customer_email = request_data['email']
    get_order.save()
    return JsonResponse({'sessionId':checkout_session.id})


class PaymentSuccessView(TemplateView):
    template_name = "cards/success_payment.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')

        if session_id is None:
            return HttpResponseNotFound()

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)
        order = get_object_or_404(Orders, stripe_payment_intent=session.payment_intent)
        order.status = 'Success'
        order.is_payment = True
        order.save()

        get_pricing = Pricing.objects.filter(id = order.price_id.id).last()
        year = int(get_pricing.validity)
        now_datetime = datetime.now()
        ex_date = now_datetime + relativedelta(years=year)

        get_card = Cards.objects.filter(id=order.card_id.id).last()
        get_card.is_active = True
        get_card.payment_status = True
        get_card.expiry_date = ex_date
        get_card.is_expire = False
        get_card.save()

        #----------- email work -----------------------------------

        url = str(request.scheme) + '://' + str(request.get_host()) + '/' + str(get_card.slug)

        ctx = {'username': get_card.user,'template_link':url,'amount':order.amount,'currency':get_card.currency}

        sub = f'Your Virtual Card is Now Online!'

        html_template = 'cards/payment_success_mail.html'

        html_message = render_to_string(html_template, ctx)

        message = EmailMessage(sub, html_message, settings.EMAIL_HOST_USER, [get_card.user.email])
        message.content_subtype = 'html'  # this is required because there is no plain text email message
        message.send()
        return render(request, self.template_name)


def PaymentFailedView(request):
    return render(request,'cards/payment_fail.html')


def PaymentSuccessPhonePayView(request):
    return render(request,'cards/success_payment.html')

#************************ Phonepay Payment Getway **************************

def callback_url(request):
    if request.method == 'POST':
        callback_data = request.POST.get('response')
        decoded_string = base64.b64decode(callback_data).decode('utf-8')
        parsed_data = json.loads(decoded_string)

        order_id = None
        if parsed_data['success'] == True:
            order_id = parsed_data['data']['merchantTransactionId']
            order = Order.objects.filter(id=order_id).last()
            order.status = 'Success'
            order.is_payment = True
            order.stripe_payment_intent = parsed_data['data']['transactionId']
            order.save()

            get_pricing = Pricing.objects.filter(id=order.price_id.id).last()
            year = int(get_pricing.validity)
            now_datetime = datetime.now()
            ex_date = now_datetime + relativedelta(years=year)

            get_card = Cards.objects.filter(id=order.card_id.id).last()
            get_card.is_active = True
            get_card.payment_status = True
            get_card.expiry_date = ex_date
            get_card.is_expire = False
            get_card.save()
            return redirect('payment_success')
        else:
            get_order = Order.objects.filter(id=order_id).last()
            get_order.status = 'Fail'
            get_order.save()
            return redirect('failed')
    else:
        return JsonResponse({'message': 'Invalid method'})


@login_required
def PaymentRecords(request):
    get_order = Orders.objects.filter(card_id__user = request.user,is_payment =True).order_by('-id')
    ctx = {
        'order':get_order,
        'websitelogo': WebSiteLogo.objects.all().last(),
        'footer': Footer.objects.all().last(),
    }
    return render(request,'cards/order_records.html',ctx)


@login_required
def EnquiryRecords(request,pk):
    get_enquiry = Enquiry.objects.filter(card_id__slug = pk).order_by('-id')
    ctx = {
        'order':get_enquiry,
        'websitelogo': WebSiteLogo.objects.all().last(),
        'footer': Footer.objects.all().last(),
    }
    return render(request,'cards/enquiry_records.html',ctx)


def CartDelete(request,pk):
    try:
        cart = Cards.objects.get(id = pk)
        cart.is_delete = True
        cart.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def ActiveDeactiveCart(request,pk):
    try:
        cart = Cards.objects.get(id = pk)
        if cart.active_deactive == False:
            cart.active_deactive = True
            cart.save()
        else:
            cart.active_deactive = False
            cart.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




