from django.conf.urls import url,include
from django.http import HttpResponse
from .views import getsquare,postnum


urlpatterns = [
    url(r'^calc/(?P<_number>\d+)',getsquare),
    url(r'^post/',postnum)

]
