from django.urls import path
from products import views 
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('',views.ProductListView.as_view()),
    path('create/',views.ProductCreateAPIView.as_view()),
    path('<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('<int:pk>/update',views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete',views.ProductDestroyAPIView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns )