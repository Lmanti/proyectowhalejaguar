from django.conf.urls import url
from CreditCardValidator import views

urlpatterns = [
    url(r'^validator/$', views.validatorAPI)
]