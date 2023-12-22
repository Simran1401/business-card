from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

def rename_file(instance, filename):
    if filename.find('.') >= 0:
        dot_index = (len(filename) - filename.rfind('.', 1)) * (-1)
        filename = filename[0:dot_index]
    filename = '{}.{}'.format(filename, 'webp')
    return filename



class PricingFeature(models.Model):
    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.title


class Pricing(models.Model):
    title = models.CharField(max_length = 200)
    amounts_INR = models.IntegerField()
    amounts_USD = models.IntegerField()
    validity = models.IntegerField()
    button = models.CharField(max_length = 150)
    features = models.ManyToManyField(PricingFeature)
    PLANTYPECHOICE = (('Individual','Individual'),('Corporate','Corporate'))
    plan_type = models.CharField(max_length = 100,choices = PLANTYPECHOICE)
    icon = models.ImageField(upload_to = 'pricing_icon/',null=True)

    def __str__(self):
        return self.title


class ClientLogo(models.Model):
    image=models.ImageField(upload_to="rename_file")


class Banner(models.Model):
    title_1=models.CharField(max_length=50)
    title_2=models.CharField(max_length=50)
    image=models.ImageField(upload_to="rename_file")
    desc=models.TextField()

    def __str__(self):
        return self.title_1
    
class About(models.Model):
    title=models.CharField(max_length=500)
    image_1=models.ImageField(upload_to="rename_file")
    image_2=models.ImageField(upload_to="rename_file",blank=True)
    desc=RichTextField()

    def __str__(self):
        return self.title
    
class Services(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="rename_file")
    desc=models.TextField()

    def __str__(self):
        return self.title
    
class Features(models.Model):
    title=models.CharField(max_length=50)
    # image=models.ImageField(upload_to="rename_file")
    icon = models.CharField(max_length = 200,null=True)

    def __str__(self):
        return self.title
    
class WhyChooseUs(models.Model):
    title=models.CharField(max_length=500)
    desc=RichTextField()

    def __str__(self):
        return self.title


heading_choice=(('About','About'),('Services','Services'),('Features','Features'),('Why_Choose_Us','Why_Choose_Us'),('Video_Section','Video_Section'),('Price','Price'))

class Heading(models.Model):
    heading_type = models.CharField(max_length=100,choices=heading_choice)
    short_title = models.CharField(max_length=100)
    main_title = models.CharField(max_length=500)
    image = models.ImageField(upload_to="rename_file",blank=True,null=True)

    def __str__(self):
        return self.heading_type

    
class Video_section(models.Model):
    title_1 = models.CharField(max_length=100)
    title_2 = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to="rename_file",blank=True)
    desc = models.TextField()
    iframe = models.CharField(max_length = 600)

    def __str__(self):
        return self.title_1


class Send_Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name


class ContactHeading(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="rename_file",blank=True)
    desc=models.TextField()

    def __str__(self):
        return self.title


class Footer(models.Model):
    phone_no = models.CharField(max_length = 20)
    whatsapp_no = models.CharField(max_length = 20,null=True)
    email = models.EmailField()
    address = models.TextField()
    twitter_link = models.URLField(blank = True)
    facebook_link = models.URLField(blank = True)
    instagram_link = models.URLField(blank = True)
    youtube_link = models.URLField(blank = True)
    image=models.ImageField(upload_to="rename__file")
    joinus_description = models.TextField(null=True,blank = True)
    footer_description = models.TextField(null=True,blank = True)


class WebSiteLogo(models.Model):
    image=models.ImageField(upload_to="rename_file")
    fav_icon = models.ImageField(upload_to="rename_file",null = True)


class Enquiry(models.Model):
    card_id = models.ForeignKey("Cards.Cards",on_delete = models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100,blank = True)
    # email = models.EmailField(null=True,blank =True)
    message = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.name


class StaticPage(models.Model):
    PAGETITLE = (('Terms-&-Conditions','Terms-&-Condition'),('Shipping-&-Delivery-Policy','Shipping-&-Delivery-Policy'),('Refund-&-Cancellation-Policy','Refund-&-Cancellation-Policy'),('Privacy-Policy','Privacy-Policy'))
    slug = models.CharField(max_length = 100,choices = PAGETITLE)
    title = models.CharField(max_length = 200,null=True)
    description = RichTextField()

    def __str__(self):
        return self.slug



class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email