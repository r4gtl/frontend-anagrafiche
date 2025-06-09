from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from app.views import ClienteViewSet, FornitoreViewSet, DashboardView

router = DefaultRouter()
router.register(r'clienti', ClienteViewSet, basename='clienti')
router.register(r'fornitori', FornitoreViewSet, basename='fornitori')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Autenticazione JWT
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # CRUD e Dashboard
    path('api/', include(router.urls)),
    path('api/dashboard/', DashboardView.as_view(), name='dashboard'),
]