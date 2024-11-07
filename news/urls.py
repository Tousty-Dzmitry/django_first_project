from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail')
    # path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-detail')
]