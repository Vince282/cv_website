from django.contrib import admin
from django.urls import path, include
from cv_app.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cv_app.urls')),
path('', home, name='home'),  # Add this line for the home page
    path('admin/', admin.site.urls),
    path('personal-info/', include('cv_app.urls')),
]

