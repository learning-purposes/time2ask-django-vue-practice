from django.contrib import admin
from django.urls import path, include, re_path
from core.views import IndexTemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),  # should be hooked to registration/login.html
    path('api-auth/', include('rest_framework.urls')), # authenticating access to browsable api
    # create a url based on regular expressions, here we need to direct
    # every request to this index.html which we will mount our vue.js to.
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]

