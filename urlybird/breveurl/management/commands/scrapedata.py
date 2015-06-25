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
from breveurl.views import shortenURL


class Command(BaseCommand):
    # this is a requirement for any admin command to extend BaseCommand
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('query', nargs='+', type=str)
    queries = ["python webbrowser module", "how to use curl in authentication", "database normalization", "educational psychology 101", "python programming jobs in durham", "search engine optimization for google", "national geographic data maps", "javascript as a programming language", "learn to program in python 101", "writing device drivers in python", "what is agile and scrum development", "beautiful soup", "pseudo-random number generators", "linear regression and statistical inference", "programming bootcamps graduates and computer science compared compared", "algorithms and heuristics"]    
    def handle(self, *args, **options):
        if options['query'][0] != 'None':
            search_strings = options['query']
        else:
            print("picked from queries")
            search_strings = self.queries
        counter = 1    
        for _ in range(50):
            search_query = random.choice(self.queries)
            results = self.get_search_text(search_query)
            
            for i in range(len(results)):
                datajson = {}
                printouts = self.pull_code_from_soup(results[i])
                if printouts is None:
                    continue
                datajson['url'] = printouts['url']
                datajson['description'] = printouts['description']
                datajson['short_description'] = printouts['short_description']
                bookmark = Bookmark()
                bookmark.url = printouts['url']
                bookmark.description = printouts['description']
                bookmark.short_description = printouts['short_description']
                bookmark.tags = search_query.split()
                bookmark.breveurl = shortenURL()
                bookmark.user = User.objects.get(pk=random.randint(1,31))
                bookmark.save()
                URL = "http://localhost:8000/api/bookmarks/"
                print("URL: {}".format(printouts['url']))
                print("Short Description: {}".format(printouts['short_description']))
                print("Description: {}".format(printouts['description']))

    def get_search_text(self, text):
        """Takes a url and returns text"""
        qry = "https://www.google.com/search?hl=en&q={}&num={}&btnG=Google+Search&gws_rd=ssl".format("+".join(text.split()), random.randint(1,15))
        req = urllib.request.Request(qry, headers={'User-Agent': 'Mozilla/5.0'})
        content = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(content)
        return soup.find_all( "li", class_="g")
        #pre is an html tag. We want all text from pre with class highlighted_source
        #returns a list of soup objects    

    def pull_code_from_soup(self, result):
        try:
            url = result.find_all("h3")
        
            short_description = result.find("a").get_text()
            title, uri = self._extract_title_url(result)
            description = result.find(class_="st").get_text()            
            return {"url":uri, "short_description":short_description, "description":description}
        except:
            return None

    def _extract_title_url(self, result):
        import re
        #title_a = result.find('a', {'class': re.compile(r'\bl\b')})
        title_a = result.find('a')
        title = ''.join(title_a.findAll(text=True))
        url = title_a['href']
        match = re.match(r'/url\?q=(http[^&]+)&', url)
        if match:
            url = match.group(1)
        return title, url
