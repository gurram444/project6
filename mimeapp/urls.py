from django.conf.urls import url
from mimeapp import views
app_name='mimeapp'
urlpatterns=[
    url(r'^csv$',views.CSVview,name='CSVview'),
    url(r'^pdf$',views.pdfview,name='pdfview'),
    url(r'^html$',views.htmlview,name='htmlview'),
    url(r'^xml$',views.xmlview,name='xmlview'),
]