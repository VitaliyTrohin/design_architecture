from typing import Any
from simba_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')


class About:
    def __call__(self, request):
        return '200 OK', 'about'
        

class Examples:
    def __call__(self, request):
        return '200 OK', render('exemples.html')


class Page:
    def __call__(self, request):
        return '200 OK', render('page.html')


class Examples:
    def __call__(self, request):
        return '200 OK', render('exemples.html')


class Another_page:
    def __call__(self, request):
        return '200 OK', render('another_page.html')


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html')                      
            