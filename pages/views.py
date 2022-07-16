from django.views.generic import TemplateView

# Create your views here.
# We need a HomePageView and a AboutPageView
# Consider: all the different things needed for these to become accessible through our web browser.

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"