from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.
# from django.http import HttpResponse
#
# def homeView(request):
#     return HttpResponse("Hello World!!!")
# def loginView(request):
#     return HttpResponse("Login Panel")

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Majharul Anwar"
        context["country"] = "Bangladesh"
        list = [1, 2, 3, 4, 5]
        context["list"] = list
        context["pageTittle"] = "Home"
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pageTittle"] = "About Us"
        return context


class BeautifullSoup(TemplateView):
    template_name = "beautifulsoup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pageTittle"] = "Beautiful Soup 4"
        import urllib.request
        with urllib.request.urlopen("http://www.python.org") as url:
            text_file = url.read()
        # textFilel = urllib.urlopen("http://www.python.org")
        # content = textFilel.read()
        soup = BeautifulSoup(text_file)
        context["links"] = soup.findAll("a")
        return context
