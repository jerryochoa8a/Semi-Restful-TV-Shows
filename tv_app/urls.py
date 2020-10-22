from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('shows/new',views.add_show_page),
    path('shows/new/add', views.add_show),
    path('shows/new/<new_show_id>',views.tv_show_page),
    path('show/new/<show_id>/edit', views.edit_show),
    path('show/new/<show_id>/edit/done', views.edit_done),

    path('show/new/<show_id>/delete', views.delete),
]