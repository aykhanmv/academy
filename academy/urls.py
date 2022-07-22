from django import views
from django.conf import settings
from django.contrib.auth import views as auth_views 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import academy, technical, fundamental, priceaction, entrytocrypto, riskmanagement, ticaretstrategy, contact, faq
from users import views as users_views
from base import views as base_views 

from users import login as login_views

import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

urlpatterns = [
    path(env('ADMIN_PAGE'), admin.site.urls),
    path('', academy, name='academy'),

    path('texniki-analiz/', technical, name='technical'),
    path('fundamental_analiz/', fundamental, name='fundamental'),
    path('price-action/', priceaction, name='priceaction'),
    path('kriptovalyutaya-giriş/', entrytocrypto, name='entrytocrypto'),
    path('riskin-idarə-edilməsi/', riskmanagement, name='riskmanagement'),
    path('ticarət-strategiyası/', ticaretstrategy, name='ticaretstrategy'),
    path('faq/', faq, name='faq'),

    path('əlaqə/', contact, name='contact'),

    path('qeydiyyat/', users_views.register, name='register'),

    path("daxil-ol", login_views.UserLoginForm, name="login"),
    path("blockchain-kabinet", login_views.UserLoginForm, name="login"),

    path('daxil-ol/blockchain-kabinet/', base_views.lobby, name='base'),
    path('çıxış-et/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),

    path('hesabım/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/done', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    path('password-reset-1/', auth_views.PasswordResetView.as_view(template_name='users/password_reset1.html'), name='password_reset1'),

    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',users_views.activate, name='activate'),  

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)