"""diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .views import Banners
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/profile/", include("app_users.urls")),
    path('api/basket', include("app_basket.urls")),
    path('api/catalog/', include("app_catalog.urls")),
    path('api/banners/', csrf_exempt(Banners.as_view())),
    path('api/categories/', include("app_catalog.urls")),
    path('api/payment/', include("app_payment.urls")),
    path('api/tags/', include("app_tags.urls")),
    path('api/orders/', include("app_orders.urls")),
    path('api/products/', include("app_products.urls")),
    path('api/payment/', include("app_payment.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('__debug__/', include('debug_toolbar.urls')),
    path("", include("frontend.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
