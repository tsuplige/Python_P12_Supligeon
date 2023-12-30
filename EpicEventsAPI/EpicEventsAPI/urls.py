from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
# from rest_framework_simplejwt.views import (TokenObtainPairView,
#                                             TokenRefreshView)

from authentication.views import UserViewSet
from api.views import ClientViewset, ContractViewset, EventViewset

router = routers.SimpleRouter()

router.register(r'clients', ClientViewset, basename='clients')
router.register(r'contracts', ContractViewset, basename='contract')
router.register(r'events', EventViewset, basename='event')
router.register(r'users',  UserViewSet, basename='users')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]

urlpatterns += router.urls