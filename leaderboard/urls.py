from django.conf.urls import url
from . import views 


urlpatterns = [ 
    url(r'',views.score_list , name='score_list'),
]

