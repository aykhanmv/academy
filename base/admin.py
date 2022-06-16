from django.contrib import admin

from base.views import room

# Register your models here.
from .models import RoomMember

admin.site.register(RoomMember)