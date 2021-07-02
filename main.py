import phonenumbers
from letstest import no

from phonenumbers import geocoder
ch = phonenumbers.parse(no,"CH")  #C=country H= history
print(geocoder.description_for_number(ch, "en"))


from phonenumbers import carrier
service_provider = phonenumbers.parse(no, "RO")
print(carrier.name_for_number(service_provider, "en"))

# To get 
