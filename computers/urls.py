from django.urls import path

from .views import ComputerDetailView, ComputerListCreateView

urlpatterns = [
    path("", ComputerListCreateView.as_view(), name="computer-list-create"),
    path("<int:pk>/", ComputerDetailView.as_view(), name="computer-detail"),
]
