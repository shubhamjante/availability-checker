import re
import requests
import pync

product_url = 'URL TO PRODUCT YOU WANT TO CHECK'

fetch_url = requests.get(product_url).text

# Replace the value of text according to unavailability of product
# if the product is unavailable
# Flipkart shows "Sold Out"
# Amazon shows "Currently unavailable"
text = "Sold Out"

product = re.findall(text, str(fetch_url))

if len(product) == 0:
    pync.Notifier.notify('Visit Site',
                         title='Product Back in Sale',
                         subtitle='Notified by python Script',
                         sound='Ping',
                         activate='com.apple.Safari')

else:
    pync.Notifier.notify('Sorry, All Sold Out',
                         title='All items Sold Out',
                         subtitle='Notified by python Script',
                         sound='Ping')
