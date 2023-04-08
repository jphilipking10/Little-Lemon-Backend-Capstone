from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

#router: DefaultRouter = DefaultRouter()
#router.register(r'scheduled', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item'),
    path('bookings/<int:pk>', views.SingleBookingView.as_view(), name='booking-detail'),
    #path('bookings/', include(router.urls)),
    path('bookings/', views.BookingViewSet.as_view(), name="booking-list"),
]


