from apscheduler.schedulers.background import BackgroundScheduler

#-------------------------###################################----------------------------

from django.utils import timezone
from datetime import date, datetime, timedelta

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.core.mail import send_mail
from django.conf import settings
from .models import *


#----------------------------------------------------------------------------------------


def OverdurCardExpirySendMail():
    get_card = Cards.objects.all()

    now_date = timezone.now().date()

    for x in get_card:
        try:
            day1 = now_date - timedelta(1)
            day7 = now_date - timedelta(7)
            ex_day = now_date
            if x.expiry_date.strftime('%Y-%m-%d') == day1.strftime('%Y-%m-%d'):
                ctx = {'username': x.user}

                sub = f'Reminder: Your Virtual Card Subscription is Expiring Soon'

                html_template = 'cards/expire_1_day.html'

                html_message = render_to_string(html_template, ctx)

                message = EmailMessage(sub, html_message, settings.EMAIL_HOST_USER, [x.user.email])
                message.content_subtype = 'html'  # this is required because there is no plain text email message
                message.send()

            elif x.expiry_date.strftime('%Y-%m-%d') == day7.strftime('%Y-%m-%d'):
                ctx = {'username': x.user}

                sub = f'Reminder: Your Virtual Card Subscription is Expiring Soon'

                html_template = 'cards/expire_7_day.html'

                html_message = render_to_string(html_template, ctx)

                message = EmailMessage(sub, html_message, settings.EMAIL_HOST_USER, [x.user.email])
                message.content_subtype = 'html'  # this is required because there is no plain text email message
                message.send()

            elif x.expiry_date.strftime('%Y-%m-%d') == ex_day.strftime('%Y-%m-%d'):
                x.is_expire = True
                x.save()

                ctx = {'username': x.user}

                sub = f'Reminder: Your Virtual Card Subscription is Expiring Soon'

                html_template = 'cards/expired.html'

                html_message = render_to_string(html_template, ctx)

                message = EmailMessage(sub, html_message, settings.EMAIL_HOST_USER, [x.user.email])
                message.content_subtype = 'html'  # this is required because there is no plain text email message
                message.send()
            else:
                pass
        except:
            pass


#--------------------------------------------------------------------------------------------------------------------

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(OverdurCardExpirySendMail ,"interval" ,hours = 24 ,replace_existing = True)
    scheduler.start()

