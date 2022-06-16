from django import views
from django.conf import settings
from django.contrib.auth import views as auth_views 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from .views import academy, technical, fundamental, priceaction, entrytocrypto, riskmanagement
from users import views as users_views
from base import views as base_views 

urlpatterns = [
    path('j898md398md3n/', admin.site.urls),
    path('', academy, name='academy'),

    path('technical/', technical, name='technical'),
    path('fundamental/', fundamental, name='fundamental'),
    path('priceaction/', priceaction, name='priceaction'),
    path('entrytocrypto/', entrytocrypto, name='entrytocrypto'),
    path('riskmanagement/', riskmanagement, name='riskmanagement'),

    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('base/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/base/', base_views.lobby, name='base'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)