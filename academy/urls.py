from django import views
from django.conf import settings
from django.contrib.auth import views as auth_views 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path 

from .views import academy, technical, fundamental, priceaction, entrytocrypto, riskmanagement, ticaretstrategy, contact, faq
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
    path('ticaretstrategy/', ticaretstrategy, name='ticaretstrategy'),
    path('faq/', faq, name='faq'),

    path('contact/', contact, name='contact'),

    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('base/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/base/', base_views.lobby, name='base'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/done', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    path('password-reset-1/', auth_views.PasswordResetView.as_view(template_name='users/password_reset1.html'), name='password_reset1'),

    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',users_views.activate, name='activate'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)