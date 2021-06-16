from django.urls import path, include
from .views import BookViewSet, AuthorViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='Books')
router.register('authors', AuthorViewSet, basename='Authors')

urlpatterns = [
    path('', include(router.urls)),
]
