from django.urls import path
from .views import (
    PostListView,
    DiseaseCreateView,
    DiseaseListView,
    DiseaseDetailView,
    DiseaseDeleteView,
    DiseaseUpdateView,
    PostDetailView,
    PostUpdateView,
    PostCreateView,
    PostDeleteView,
    HerbListView,
    HerbCreateView,
    HerbDetailView,
    HerbUpdateView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='Post_detail'),
    path('post/new/', PostCreateView.as_view(), name='create_view'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='Post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='Post_delete'),
    path('disease/', DiseaseListView.as_view(), name='disease'),
    path('disease/new/', DiseaseCreateView.as_view(), name='disease_view'),
    path('disease/<int:pk>/', DiseaseDetailView.as_view(), name='Disease_detail'),
    path('disease/<int:pk>/delete/', DiseaseDeleteView.as_view(), name='Disease_delete'),
    path('disease/<int:pk>/update/', DiseaseUpdateView.as_view(), name='Disease-update'),
    path('Herb/new/', HerbCreateView.as_view(), name='herb_view'),
    path('Herb/', HerbListView.as_view(), name='herb'),
    path('Herb/<int:pk>/', HerbDetailView.as_view(), name='herb_detail'),
    path('Herb/<int:pk>/update/', HerbUpdateView.as_view(), name='herb-update'),
]
