import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakergen = Faker()

def populate(N = 5):

    for entry in range(N):
        first_name = fakergen.user_name()
        last_name = fakergen.user_name()
        email = fakergen.email()
        userModel = User.objects.get_or_create(first_name = first_name, last_name = last_name, email = email)

if __name__ == '__main__' :
    print('population Script is running')
    populate(20)
    print('population complete')