from django.urls import path
from django.views.generic import TemplateView

# Note: "In the Django framework, views are Python functions or classes that takes a web request and returns a web response. 
# This response can be the HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really."
urlpatterns = [
    path('',
         # The TemplateView class renders a given template & the as_view() function overrides attributes set on the class
         # We set the TemplateView attribute template_name to 'cards/base.html' here so that base.html is rendered by TemplateView
         TemplateView.as_view(template_name='cards/base.html'),
         # Using the name argument allows us to refer to this route as 'home' instead of its url
         name='home'
         )
]
