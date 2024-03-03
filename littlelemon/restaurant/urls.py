from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet)

urlpatterns += router.urls