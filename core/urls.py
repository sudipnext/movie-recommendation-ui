from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ProfileViewSet, MovieViewSet, FavoriteViewSet,
                   RatingViewSet, CommentViewSet, WatchListViewSet)

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'movies', MovieViewSet)
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'ratings', RatingViewSet, basename='rating')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'watchlist', WatchListViewSet, basename='watchlist')

urlpatterns = [
    path('', include(router.urls)),
] 