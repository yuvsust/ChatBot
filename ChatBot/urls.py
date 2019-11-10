
from django.contrib import admin
from django.urls import path
from webhook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('webhook/', views.webhook, name='webhook'),

]
