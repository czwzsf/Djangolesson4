from django.urls import path

from system import views

urlpatterns = [
    path('slider/list/', views.slider_list, name="slider_list"),
    path('cache/set/', views.cache_set, name="cache_set"),
    path('cache/get/', views.cache_get, name="cache_get"),
]
