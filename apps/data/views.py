from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    out = """
    <p>this is just hello world
    <p>solid i18n urls does a lot of things.
    <p>one thing is throws 404 for unsupported languages automatically
    <p>i have
    <p>LANGUAGES = (('en', 'English'), ('de', 'German'),)
    <p> in my settings.

    <p>supported languages:
    <p><a href="http://127.0.0.1:8000/en/main/">english</a>
    <p><a href="http://127.0.0.1:8000/de/main/">german</a>

    <p>unsupported languages:
    <p>for all other langues it gives 404 page.
    <p>for example:
    <p><a href="http://127.0.0.1:8000/ru/main/">russian</a>
    <p><a href="http://127.0.0.1:8000/te/main/">telugu</a>
    
    """
    return HttpResponse(out)
