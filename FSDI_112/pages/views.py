from re import template
from django.views.generic import TemplateView

#Homepaveview is extending templateview
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'