

from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include

from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'register', views.RegisterAPI)


urlpatterns = [
      path('', include(router.urls))

      #path('auth/register/', views.RegisterAPI.as_view, name='register'),

]