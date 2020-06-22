from django.urls import path

from demo import views


urlpatterns = [
    path('', views.render_view),
    path('data/', views.data_view),
    path('form-data/', views.form_data_view),
]
