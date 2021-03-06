from django.urls import path
from .views import (
    UsersListView,
    UsersDetailView,
    UsersCreateView,
    UsersUpdateView,
    UsersDeleteView,
    HomeView
)

# Create your urls here.
# Add the class in views.py as View
app_name='users'
urlpatterns = [
    path('',HomeView.as_view(), name='user-list'),
    path('lista-de-usuarios',UsersListView.as_view(), name='user-list'),
    path('<int:id>/',UsersDetailView.as_view(), name='user-detail'),
    path('crear/',UsersCreateView.as_view(),name='user-create'),
    path('<int:id>/actualizar/',UsersUpdateView.as_view(), name='user-update'),
    path('<int:id>/borrar/',UsersDeleteView.as_view(), name='user-delete'),
]
