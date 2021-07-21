import phonenumbers

# geocoder: to know the specific
# location to that phone number
from phonenumbers import geocoder

phone_number = phonenumbers.parse("Number with country code")
# Indian phone number example: +91**********
# Nepali phone number example: +977**********


# this will print the country name
print(geocoder.description_for_number(phone_number,'en'))
