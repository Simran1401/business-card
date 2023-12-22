from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView

urlpatterns = [

    path('',views.home,name="home"),
    path('send/',views.post_contact,name="send"),
    path('signup/',views.Signup,name="signup"),
    path('signin/',views.Signin,name="signin"),
    path('signout/',views.Signout,name="signout"),
    # path('table/',views.Table_view,name="table"),
    # path('index/<slug>/',views.Index,name="index"),
    path('enquiry',views.Post_enquiry,name="enquiry"),
    path('subscribe',views.SubscribeView,name="subscribe"),
    path('forgot_password',views.ForgetPassword,name="forgot_password"),
    path('about-us',views.AboutPageview,name="about_us"),
    path('contact-us',views.ContactUsPageview,name="contact_us"),

    path('<id>/',views.StaticPageView,name="static_page")

  
]
