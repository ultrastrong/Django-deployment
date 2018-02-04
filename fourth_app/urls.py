from django.conf.urls import url
from fourth_app import views


urlpatterns = [
    url(r'^registration/', views.registration, name='registration'),
    url(r'^user_login/', views.user_login, name='user_login')
]
