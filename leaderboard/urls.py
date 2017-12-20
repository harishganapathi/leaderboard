from django.conf.urls import url
from . import views 


urlpatterns = [ 
    url(r'^$',views.score_list , name='score_list'),
    url(r'^score/(?P<pk>\d+)/$', views.score_detail, name='score_detail'),
    url(r'^score/new$', views.new_score , name = 'new_score'),
    url(r'^score/(?P<pk>\d+)edit$', views.score_edit, name='score_edit'),
    url(r'^score/(?P<pk>\d+)delete$', views.score_delete, name='score_delete')

]


