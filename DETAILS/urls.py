from django.conf.urls import include, url
from .views import getsubject,getstudentname,getmathstopper,getengavg,getmintotal,getmathtopper,getfachigh
from .views import getstudentid,getstudentmarks,facultydata,getrange,studentdata,getmarks,getsubavg,getsum,getmaxtotal,getsubninty,getfacleast
from .rest_api import test, studentlist,studentmarks,ninty,gettotal,mathtop,subavg,sum,maxtotal,mintotal,fachigh,facleast,subninty
urlpatterns =[

     url(r'^studentid/(?P<_id>\d+)', getstudentid),
     url(r'^studentname/(?P<_studentname>[\w\-]+)/$', getstudentname),
     url(r'^subject/(?P<_subject>[\w\-]+)/$',getsubject),
     url(r'^subjectfaculty/',facultydata),
     url(r'^studentmarks/',studentdata),
     url(r'^marks/(?P<_marks>\d+)', getmarks),
     url(r'^range/',getrange),
     url(r'^stunt/(?P<_range>[0-99,-]+)',getstudentmarks),
     url(r'^maths/',getmathstopper),
     url(r'^sum/',getsum),
     url(r'^maxtotal/',getmaxtotal),
     url(r'^mintotal/',getmintotal),
     url(r'^avgsub/',getsubavg),
     url(r'^math',getmathtopper),
     url(r'^eng/(?P<_subjectname>[\w\-]+)/$',getengavg),
     url(r'^sub/',getsubninty),
     url(r'^least/',getfacleast),
     url(r'^high/',getfachigh),
     #url(r'^sub90/',getsubwith90),
         #rest_api
     url(r'^ninty/',ninty),
     url(r'^test/', test),
     url(r'^students/',studentlist),
     url(r'^getmarks/(?P<_marks>\d+)', studentmarks),
     url(r'^total/',gettotal),
     url(r'^top/',mathtop),
     url(r'^list/',subavg),
     url(r'^stu/',sum),
     url(r'^bright/',maxtotal),
     url(r'^can/',mintotal),
     url(r'^counttop/',fachigh),
     url(r'^countleast/',facleast),
     url(r'^countninty/',subninty)


     #url(r'^total/',total)
]
