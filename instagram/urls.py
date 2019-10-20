from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    #  url(r'^instagram/post$', views.new_post, name='new_post')
     url(r'^new/post$', views.new_post, name='new-post'),
]