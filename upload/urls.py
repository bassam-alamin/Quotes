from django.conf.urls import url
from . import views



app_name = 'upload'

urlpatterns = [
    #/home/
    url(r'^$',views.home.as_view(),name='home'),
    #/home/register
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    #home/login
    url(r'^login/$',views.LoginUser.as_view(),name='login'),

    url(r'^logout/$',views.logoutuser,name='logout'),




    #/home/712/

    url(r'^(?P<pk>[0-9]+)/$',views.detail.as_view(), name= 'detail'),

    #/home/add/

    url(r'^add/$',views.AuthorCreate.as_view(),name='author-add'),

    #home/update/6
    url(r'^update/(?P<pk>[0-9]+)/$',views.AuthorUpdate.as_view(),name='author-update'),
    #home/update/6
    url(r'^(?P<pk>[0-9]+)/delete$', views.AuthorDelete.as_view(), name='author-delete'),

    url(r'^quote/add/$',views.SayingCreate.as_view(),name='saying-add'),

    url(r'^edit/(?P<pk>[0-9]+)/$',views.SayingUpdate.as_view(),name='saying-edit'),



]
