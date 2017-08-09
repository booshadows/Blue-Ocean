from django.conf.urls import include, url
from django.contrib import admin
from BlueOcean import views as BlueOcean_views

urlpatterns = [
    url(r'^$', BlueOcean_views.hello),
    url(r'^article/$', BlueOcean_views.index), 
    url(r'^admin/', admin.site.urls),
]