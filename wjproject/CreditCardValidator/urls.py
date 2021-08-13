from django.conf.urls import url
from CreditCardValidator import views

# Se establece la ruta a consultar desde el front
urlpatterns = [
    url(r'^validator/$', views.validatorAPI)
]