from django.urls import path,include
from rest_framework.routers import DefaultRouter


from .views import CustomerViewSet, CategoryViewSet, AddViewSet, AddPicViewSet


router = DefaultRouter()


router.register('customer', CustomerViewSet)
router.register('category', CategoryViewSet)
router.register('add', AddViewSet)
router.register('add_pic', AddPicViewSet)


urlpatterns = [
    path('', include(router.urls)),
]