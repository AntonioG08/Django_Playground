"""
URL configuration for webplayground project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    # Paths for auth, with this we can use the urls for authentication that Django offers
    path('accounts/', include('django.contrib.auth.urls')),
    # With this we add additional possile paths for 'accounts' to include also de registration ones
    path('accounts/', include('registration.urls')),
]
