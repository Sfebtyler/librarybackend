from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework.authtoken import views as authview
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'books', views.BooksViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', authview.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
