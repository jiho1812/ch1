
from django.contrib import admin
from django.urls import path
from points.views import add_points

urlpatterns = [
    path('admin/', admin.site.urls),
    path('points/', add_points, name='add_points'),
]
