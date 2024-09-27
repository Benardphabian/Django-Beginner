from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('App1.urls')),
    path('app2/', include('App2.urls')),
]
