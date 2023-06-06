from django.urls import path, include
from product import views

app_name = 'product'

urlpatterns = [
    path('latest-products', views.LatestProductList.as_view()),

]
