from django.db import models
from config.models import *
from Accounts.models import *
from PIL import Image

# Create your models here.

currency_choice=(('INR','INR'),('USD','USD'))
QR_choices=(('GooglePay','GooglePay'),('Paytm','Paytm'),('Phonepe','Phonepe'),('Other','Other'))


def rename_file(instance, filename):
    if filename.find('.') >= 0:
        dot_index = (len(filename) - filename.rfind('.', 1)) * (-1)
        filename = filename[0:dot_index]
    filename = '{}.{}'.format(filename, 'webp')
    return filename


class BusinessNature(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Cards(models.Model):
    user = models.ForeignKey(User,on_delete = models.PROTECT)
    slug = models.SlugField(null=True,blank=True,unique= True)
    payment_status = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False,null=True)
    views = models.IntegerField(default = 0)
    expiry_date = models.DateField(null=True,blank= True)
    is_expire = models.BooleanField(default = False,null=True)
    currency = models.CharField(max_length = 50 ,null=True)
    is_delete =  models.BooleanField(default = False,null=True)
    active_deactive = models.BooleanField(default = True,null=True)

    def __str__(self):
        return self.user.username

    def get_basicInfo(self):
        obj = ComInfo.objects.filter(card_id = self.id).last()
        return obj


class ComInfo(models.Model):
    card_id = models.ForeignKey(Cards,on_delete = models.PROTECT)
    company_name = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100,null=True)
    # slug=models.CharField(max_length=350,null=True,blank=True,unique=True)
    designation=models.CharField(max_length=100,blank=True,null=True)
    contact_number_1 = models.CharField(max_length=50,null=True)
    contact_number_2 = models.CharField(max_length=50,blank=True,null=True)
    whatsapp_number_1 = models.CharField(max_length=50,blank=True,null=True)
    whatsapp_number_2 = models.CharField(max_length=50, blank=True,null=True)

    landline_number = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(null=True)
    website_url=models.CharField(max_length = 800,blank=True,null=True)
    google_map_link = models.CharField(max_length = 600,null = True,blank=True)
    profile_picture = models.ImageField(upload_to=rename_file,null=True)
    logo = models.ImageField(upload_to=rename_file,null=True)

    city=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=50,null=True)
    # country_code = models.CharField(max_length=50,null=True,default = '91')
    address=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.company_name


class Social(models.Model):
    card_id =models.ForeignKey(Cards,null=True,on_delete=models.PROTECT,blank=True)
    facebook = models.CharField(max_length = 600,null = True,blank=True)
    instagram = models.CharField(max_length = 600,null = True,blank=True)
    twitter = models.CharField(max_length = 600,null = True,blank=True)
    pinterest = models.CharField(max_length = 600,null = True,blank=True)
    youtube = models.CharField(max_length = 600,null = True,blank=True)
    linkedin = models.CharField(max_length = 600,null = True,blank=True)
    video_link = models.CharField(max_length = 600,null = True,blank=True)


class AboutInfo(models.Model):
    card_id =models.ForeignKey(Cards,null=True,on_delete=models.PROTECT,blank=True)
    estblishment_year = models.DateField(null=True,blank=True)
    business_nature = models.ForeignKey("BusinessNature", on_delete=models.CASCADE)
    GSTIN_No = models.CharField(max_length=20, blank=True)
    document_name = models.CharField(max_length = 200,blank=True,null=True)
    upload_documents = models.FileField(upload_to="documents",blank=True,null=True)
    Desc = RichTextField(blank=True)

    def __str__(self):
        return self.business_nature.title


class ProductAndService(models.Model):
    card_id =models.ForeignKey(Cards,null=True,on_delete=models.PROTECT,blank=True)
    name = models.CharField(max_length = 200 , null=True)
    Currency = models.CharField(choices=currency_choice, max_length=100, blank=True)
    price = models.CharField(max_length = 200,blank=True, null=True)
    PSTYPE = (('Product','Product') , ('Service','Service'))
    type = models.CharField(max_length=50, choices = PSTYPE,null=True)
    image = models.ImageField(upload_to="rename_file")

    def __str__(self):
        return self.name


class BankDetail(models.Model):
    card_id = models.ForeignKey(Cards,null=True,on_delete=models.PROTECT,blank=True)
    bank_name = models.CharField(max_length=50, blank=True,null=True)
    branch_name = models.CharField(max_length=50, blank=True,null=True)
    Ac_holder_name = models.CharField(max_length=50, blank=True,null=True)
    Account_number = models.CharField(max_length = 100,null=True)
    IFSC_code = models.CharField(max_length=50, blank=True, null=True)
    ACTYPECHOICE = ('Savings Account','Savings Account'),('Current Account','Current Account') , ('Salary Account','Salary Account'), ('Fixed Deposit Account','Fixed Deposit Account'), ('Recurring Deposit Account','Recurring Deposit Account'), ('NRO - Savings Accounts','NRO - Savings Accounts'), ('NRO - Fixed Deposit Accounts','NRO - Fixed Deposit Accounts'), ('NRE - Savings Accounts','NRE - Savings Accounts'), ('NRE - Fixed Deposit Accounts','NRE - Fixed Deposit Accounts'), ('FCNR - Account','FCNR - Account')
    account_type = models.CharField(max_length=50,choices = ACTYPECHOICE, blank=True,null=True)
    IBAN_number = models.CharField(max_length = 100,blank=True, null=True)
    SWIFT_code = models.CharField(max_length = 100,blank=True, null=True)
    type_of_QR = models.CharField(choices=QR_choices, max_length=50,null=True,blank=True)
    uplaod_QR_image = models.ImageField(upload_to="rename_file", blank=True,null=True)
    payment_number = models.CharField(max_length = 100,blank=True, null=True)
    UPI_number = models.CharField(max_length = 100,null=True)


class Gallery(models.Model):
    card_id =models.ForeignKey(Cards,null=True,on_delete=models.PROTECT,blank=True)
    image = models.ImageField(upload_to=rename_file,null=True)


class TemplateBackgroundImage(models.Model):
    image = models.ImageField(upload_to="rename_file",null=True)


class Setting(models.Model):
    card_id =models.ForeignKey(Cards,null=True,on_delete=models.PROTECT,blank=True)
    view_count = models.BooleanField(default = True)
    about_us_section = models.BooleanField(default = True)
    prodcut_and_service_section = models.BooleanField(default = True)
    payment_option_section = models.BooleanField(default = True)
    gallery_section = models.BooleanField(default = True)
    video_section = models.BooleanField(default = True)
    enquiry_section = models.BooleanField(default = True)
    # show_menu = models.BooleanField(default = False)
    color = models.CharField(max_length = 50,null=True)
    font_color = models.CharField(max_length = 50,null=True)
    primary_font = models.CharField(max_length = 50,null=True)
    secondry_font = models.CharField(max_length = 50,null=True)
    bg_image = models.ForeignKey(TemplateBackgroundImage,on_delete = models.PROTECT,null=True,blank = True)


class Config(models.Model):
    product_number = models.IntegerField(default = 9)
    gallery_image = models.IntegerField(default = 9)
    card_expiry_days = models.IntegerField(default = 30)


class PaymentOfCard(models.Model):
    card_id = models.ForeignKey(Cards,on_delete = models.PROTECT)
    STATUS = (('Success','Success'),('Fail','Fail'))
    payment_status = models.CharField(max_length = 200 ,choices = STATUS)
    user = models.ForeignKey(User,on_delete = models.PROTECT)

    pricing_id = models.ForeignKey(Pricing,on_delete = models.PROTECT)
    amounts_INR = models.IntegerField()
    amounts_USD = models.IntegerField()
    validity = models.IntegerField()
    features = models.ManyToManyField(PricingFeature)
    PLANTYPECHOICE = (('Individual', 'Individual'), ('Corporate', 'Corporate'))
    plan_type = models.CharField(max_length=100, choices=PLANTYPECHOICE)
    icon = models.ImageField(upload_to='pricing_icon/', null=True)

    def __str__(self):
        return self.payment_status


class Orders(models.Model):
    card_id = models.ForeignKey(Cards,on_delete = models.PROTECT)
    price_id = models.ForeignKey(Pricing,on_delete = models.PROTECT)
    stripe_payment_intent = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(null=True)
    validity = models.IntegerField(null=True)
    features = models.ManyToManyField(PricingFeature,null=True)
    datetime = models.DateField(auto_now_add = True)
    PAYMENTSTATUS = (('Success','Success') , ('Fail','Fail'))
    status = models.CharField(max_length = 200,choices = PAYMENTSTATUS,null=True)
    is_payment = models.BooleanField(default = False)




