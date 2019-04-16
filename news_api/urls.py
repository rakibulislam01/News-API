"""news_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'url', views.TopNewspaper, basename='url')
router.register(r'hotnews', views.TopNewsTopic, basename='hotnews')
router.register(r'LatestNews', views.LatestNews, basename='LatestNews')
router.register(r'EducationNews', views.TopEducationNews, basename='EducationNews')
router.register(r'TopKoreanNews', views.TopKoreanNews, basename='TopKoreanNews')
router.register(r'DailyStarTopNews', views.DailyStarTopNews, basename='DailyStarTopNews')
router.register(r'BanglaBccNews', views.BanglaBccNews, basename='BanglaBccNews')
router.register(r'JapanBccNews', views.JapanBccNews, basename='JapanBccNews')
router.register(r'AllNews', views.AllNews, basename='AllNews')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
