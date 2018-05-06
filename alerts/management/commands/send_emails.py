"""
Management command to check alerts in DB and send emails
"""

import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from alerts.models import Alert

class Command(BaseCommand):
    """
    Check all alerts in DB and send email if needed
    """
    help = 'Check all alerts in DB and send email if needed'

    def handle(self, *args, **options):
        now = datetime.datetime.now()
        minutes = [2, 10, 30]
#        minutes = [2]
        results = []
        for minute in minutes.copy():
            if (now.minute % minute) != 0:
#                minutes.remove(minute)
                print(minute, now.minute, now.minute % minute, (now.minute % minute) == 0)
        for minute in minutes:
            for alert in Alert.objects.filter(update_time=minute):
                print("searching ebay for {}".format(alert.phrase))
                for ebay_item in ebay_search(alert.phrase):
                    title = ebay_item.get('title')
                    item_id = ebay_item.get('itemId')
                    url = ebay_item.get('viewItemURL')
                    end_time = ebay_item.get('listingInfo').get('endTime')
                    price = float(ebay_item.get('sellingStatus').get('currentPrice').get('value'))
                    results.append([price, item_id, title, url, end_time])
                send_email(alert.user_email, sorted(results)[:20])

def send_email(user_email, results):
    """
    Send a list of results to the given email address
    """
    subject = "Ebay update for {}".format(datetime.datetime.now())
    message = render_to_string('email.html', {'email': user_email, 'results': results})
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email, ], fail_silently=False,
              html_message=message)

def ebay_search(keywords):
    """
    Search Ebay for given keywords.
    returns: list of items
    """

    try:
        api = Connection(appid=settings.EBAY_API_KEY, config_file=None)
        response = api.execute('findItemsAdvanced', {'keywords': keywords})

        assert response.reply.ack == 'Success'
        assert isinstance(response.reply.timestamp, datetime.datetime)
        assert isinstance(response.reply.searchResult.item, list)
        assert isinstance(response.dict(), dict)
        items = response.reply.searchResult.item
        return items

    except ConnectionError:
        return None
