from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('list', views.PostList.as_view(), name='list'),
    path('', views.PostList.as_view(), name='list'),
    path('new/', views.PostCreate.as_view(), name='create'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('<int:pk>/delete', views.PostDelete,name='delete'),
    path('search_data', views.search_view, name='search'),

]
