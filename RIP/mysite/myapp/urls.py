"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^test/', views.hello, name='hello'),
    url(r'^startpage/', views.main, name='main'),
    url(r'^choice/', views.choice, name='choice'),
    url(r'^extra/(?P<band_id>\d+)', views.Extra.as_view(), name='extra'),
    url(r'^join/(?P<band_id>\d+)', views.join, name='send'),
    url(r'^index/$', views.PrivateBandList.as_view(), name='index'),
    url(r'^index/page=(?P<page>\d+)', views.PrivateBandList.as_view(), name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'modal_window2.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'main'}, name='logout'),
    url(r'^band_adding/$', views.BandAddingView.as_view(), name='band_adding'),
    url(r'^artist/$', views.Artist_Data.as_view(), name='artist_data'),
    url(r'^artist_adding/$', views.ArtistAddingView.as_view(), name='artist_adding'),
    url(r'^error/$', views.ErrorView.as_view(), name='error_page'),
]
