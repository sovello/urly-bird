from django.core.management.base import BaseCommand, CommandError
from breveurl.models import Bookmark

# Scraping tools
import random
from bs4 import BeautifulSoup
import requests
import urllib
from re import findall
import random
import json
from django.contrib.auth.models import User
from faker import Factory
fake = Factory.create()

class Command(BaseCommand):
    # this is a requirement for any admin command to extend BaseCommand
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('number', nargs='+', type=int)

    def handle(self, *args, **options):
        number = int(options['number'][0])
        print(options['number'])
        for i in range(number):
            print("Creating user {} of {}".format(i+1, number))
            user = User()
            user.username = self.get_username()
            user.password = "password"
            user.email = fake.email()
            user.save()
        print("Done. Created {} users".format(i+1))

    def get_username(self):
        name = fake.name().split()[-1].lower()
        if User.objects.filter(username=name):
            return self.get_username()
        else:
            return name
