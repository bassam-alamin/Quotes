from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from upload import views




urlpatterns = [
    url(r'^$',views.home.as_view(),name='home'),
    url(r'^home/',include('upload.urls')),
    url(r'^admin/', admin.site.urls),


]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


