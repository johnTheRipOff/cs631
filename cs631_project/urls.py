from django.contrib import admin
from django.urls import include, path
from patient.views import *




urlpatterns = [
    path('patient/', include('patient.urls')),
    path('admin/', admin.site.urls),
]
