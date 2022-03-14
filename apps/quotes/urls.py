from django.conf.urls import url
# from django.urls import path
from .import views
from apps.quotes.views import quotesCreate, quotesDelete, quotesEdit, quotesList, quotesHome, quotesDetail

urlpatterns = [
    url(r'^create', quotesCreate.as_view(), name='quotesCreate'),
    url(r'^delete/(?P<pk>\d+)/', quotesDelete.as_view(), name='quotesDelete'),
    url(r'^edit/(?P<pk>\d+)/', quotesEdit.as_view(), name='quotesEdit'),
    url(r'^list', reportList.as_view(), name='quotesList'),
    url(r'^home', reportHome.as_view(), name='quotesHome'),
    url(r'^detail/(?P<pk>\d+)/$', quotesDetail.as_view(), name='quotesDetail'),



]