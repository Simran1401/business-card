# from django import forms
#
# from .models import *
#
#
#
# class DateInput(forms.DateInput):
#     input_type = 'date'
#
#
# class ComInfoForms(forms.ModelForm):
#     address = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':20}))
#
#     class Meta:
#         model = ComInfo
#         exclude = ('card_id',)
#
#         widgets = {
#             'contact_number_1': forms.TextInput(attrs={'type': 'number'}),
#             'contact_number_2': forms.TextInput(attrs={'type': 'number'}),
#             'whatsapp_number_1': forms.TextInput(attrs={'type': 'number'}),
#             'whatsapp_number_2': forms.TextInput(attrs={'type': 'number'}),
#             'landline_number': forms.TextInput(attrs={'type': 'number'}),
#         }
#
#
# class SocialForms(forms.ModelForm):
#     class Meta:
#         model = Social
#         exclude = ('card_id',)
#
#
# class AboutInfoForms(forms.ModelForm):
#     class Meta:
#         model = AboutInfo
#         exclude = ('card_id',)
#
#         widgets = {
#             'estblishment_year':DateInput,
#
#         }
#
#
# class ProductAndServiceForms(forms.ModelForm):
#     class Meta:
#         model = ProductAndService
#         exclude = ('card_id',)
#
#
# class BankDetailForms(forms.ModelForm):
#     class Meta:
#         model = BankDetail
#         exclude = ('card_id',)
#
#
# class GalleryForms(forms.ModelForm):
#     class Meta:
#         model = Gallery
#         exclude = ('card_id',)
#
#
# class SettingForms(forms.ModelForm):
#     class Meta:
#         model = Setting
#         fields = ('view_count','about_us_cection','prodcut_and_service_section','payment_option_section','gallery_section','video_section','enquiry_section','show_menu')
#         # exclude = ('card_id',)
#
#
