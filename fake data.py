# use fake data

from faker import Faker

name = Faker()
adress = Faker()
email = Faker()

print(name.name())
print(adress.address())
print(email.email())