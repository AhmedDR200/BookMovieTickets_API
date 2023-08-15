"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # way 1
    path('django/json-no-model/', views.no_rest_no_model, name="no-no"),
    # way 2
    path("django/json-from-model/", views.no_rest_from_model, name="no-from"),
    # way 3 (FBV)--> GET , POST
    path("rest/fbv_list/", views.fbv_list, name="fbv_rest_list"),
    # way 4 (FBV)--> GEt , PUT , DELETE
    path("rest/fbv_detail/<int:pk>", views.fbv_detail, name="fbv_rest_detail"),
    # way 5 (CBV)--> GET , POST
    path("rest/cbv_list/", views.CBV_List.as_view(), name="cbv_rest_list"),
    # way 5 (CBV)--> GET , PUT , DELETE
    path("rest/cbv_detail/<int:pk>", views.CBV_Detail.as_view(), name="cbv_rest_detail"),
    # way 6 (CBV/mixins-generics)--> GET , POST 
    path("rest/cbv-mixins_list/", views.Mixins_list.as_view(), name="cbv-mixins_list"),
    # way 6 (CBV/mixins-generics)--> GET , PUT , DELETE
    path("rest/cbv-mixins_detail/<int:pk>", views.Mixins_Detail.as_view(), name="cbv-mixins_detail"),
]
