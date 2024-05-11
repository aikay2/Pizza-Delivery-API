from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name="orders"),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name="order-detail"),
    path('update-status/<int:order_id>/', views.UpdateOrderStatusView.as_view(), name="update-order-status"),
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view(), name="users-orders"),
    path('user/<int:user_id>/order/<int:order_id>/', views.UserOrderDetailView.as_view(), name="users-orders-detail"),
]
