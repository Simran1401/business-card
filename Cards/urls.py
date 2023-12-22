from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('dashboard', views.MyDashboard, name='mycard'),
    path('create_card', views.CreateCard, name='create_card'),
    path('add_company_info/<int:pk>', views.AddComInfoView, name='add_company_info'),
    path('add_social_video/<int:pk>', views.AddSocialView, name='add_social_video'),
    path('add_about/<int:pk>', views.AddAboutInfoView, name='add_about'),
    path('add_bank_detail/<int:pk>', views.BankDetailView, name='add_bank_detail'),
    path('add_product_and_service/<int:pk>/<id>', views.ProductServiceView, name='add_product_and_service'),
    path('delete_product_and_service/<int:pk>/<id>', views.ProductServiceDeleteView, name='delete_product_and_service'),
    path('add_gallery/<int:pk>/<id>', views.GalleryView, name='add_gallery'),
    path('delete_gallery/<int:pk>/<id>', views.GaleryDeleteView, name='delete_gallery'),
    path('add_setting/<int:pk>', views.SettingView, name='add_setting'),

    path('payment_records',views.PaymentRecords,name='payment_records'),
    path('enquiry_records/<pk>',views.EnquiryRecords,name='enquiry_records'),
    path('card_pricing/<int:pk>',views.CardPricing,name='card_pricing'),

    path('checkout_card/<int:card_id>/<int:price_id>/',views.CheckoutCart,name='checkout_card'),

    path('payment/success/',PaymentSuccessView.as_view(), name='success'),

    path('payment/failed/',views.PaymentFailedView, name='failed'),
    path('payment/success/',views.PaymentSuccessPhonePayView, name='payment_success'),

    path('create_checkout_session/<int:id>',views.create_checkout_session,name='create_checkout_session'),

    path('<slug>',views.CardTemplateView,name='card_template_view'),

    path('card_delete/<int:pk>',views.CartDelete,name='card_delete'),
    path('card_active_deactive/<int:pk>',views.ActiveDeactiveCart,name='card_active_deactive')

]
