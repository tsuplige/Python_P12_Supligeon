from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
# from rest_framework_simplejwt.views import (TokenObtainPairView,
#                                             TokenRefreshView)

from authentication import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls