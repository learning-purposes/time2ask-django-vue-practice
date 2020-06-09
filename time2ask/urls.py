from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # make the homepage is the home in users app
    # path('accounts/', include('django.contrib.auth.urls')),  # should be hooked to registration/login.html
    path('api-auth/', include('rest_framework.urls')), # authenticating access to browsable api
]

