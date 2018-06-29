from django.conf.urls import url,include
from django.http import HttpResponse
from .views import getsquare,postnum,cal_list,comp


urlpatterns = [
    url(r'^calc/(?P<_number>\d+)',getsquare),
    url(r'^post/',postnum),
    url(r'^list/(?P<_number>\d+)',cal_list),
    url(r'^stat/(?P<_values>[0-99,-]+)',comp),

]
