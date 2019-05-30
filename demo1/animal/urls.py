from django.conf.urls import include,url
from . import views
from . import feed


app_name='animal'
urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'^single/(\d+)/$',views.single,name='single'),
    url(r'^comment/(\d+)/$',views.comment,name='comment'),
    url(r'^classify/(\d+)/$',views.classify,name='classify'),
    url(r'^recent/(\d+)/$', views.recent, name='recent'),
    url(r'^file/(\d+)/(\d+)/$', views.file, name='file'),
    url(r'^label/(\d+)/$',views.label,name='label'),
    url(r'^indeximg/$',views.indeximg,name='indeximg'),
    url(r'^gallery/$',views.gallery,name='gallery'),
	url(r'^rss/$',feed.animalFeed(),name='rss'),
    url(r'^about/$',views.about,name='about'),
    url(r'contact',views.contact,name='contact'),
    url(r'icons',views.icons,name='icons'),
    url(r'typography',views.typography,name='typography'),
    url(r'^contacts/$',views.Contacts.as_view(),name='contacts'),




]