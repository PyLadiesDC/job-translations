from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.job_translation, name='job_translation'),
]
