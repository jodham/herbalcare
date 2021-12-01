from django.urls import path
from .views import (
    PostListView,
    DiseaseCreateView,
    DiseaseDetailView,
    DiseaseListView,
    HerbCreateView,
    PostDetailView,
    PostUpdateView,
    PostCreateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('disease/', DiseaseListView.as_view(), name='disease_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='Post_detail'),
    path('disease/<int:pk>/', DiseaseDetailView.as_view(), name='disease_detail'),
    path('post/new/', PostCreateView.as_view(), name='create_view'),
    path('disease/new/', DiseaseCreateView.as_view(), name='disease_view'),
    path('Herb/new/', HerbCreateView.as_view(), name='herb_view'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='Post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='Post_delete')
]
