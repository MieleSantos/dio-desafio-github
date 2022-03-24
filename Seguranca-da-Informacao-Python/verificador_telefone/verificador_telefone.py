import phonenumbers
from phonenumbers import geocoder

"""
Descobrindo a localização do número do telefone
"""
phone = input("Digiten o teleone no formato +550000000000: ")

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, "pt"))
