from django.urls import path
from .views import (JournalistListCreateAPIView,
                    # article_list,
                    # article_details,
                    ArticleListCreateAPIView,
                    ArticleDetailsAPIView)

urlpatterns = [
    # path('atricles/', article_list, name='article_list'),
    # path('atricles/<int:pk>/', article_details, name='article_details'),

    path('atricles/', ArticleListCreateAPIView.as_view(), name='ArticleListCreate'),
    path('atricles/<int:pk>/', ArticleDetailsAPIView.as_view(), name='ArticleDetails'),
    path('journalist/', JournalistListCreateAPIView.as_view(), name='JournalistListCreate'),

]
