from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('shows', views.index),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:show_id>', views.show),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/update', views.update),
    path('shows/<int:show_id>/delete', views.destroy),
]