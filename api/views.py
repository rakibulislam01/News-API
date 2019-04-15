from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response as RestResponse

from .google_news import top_news_title, top_education_news
from .popular_newspaper import popular_paper, hot_news
from .serializers import UserSerializer, GroupSerializer
from .korean import top_news_korean


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TopNewspaper(viewsets.ViewSet):
    def list(self, request):
        newspapers = request.GET.get('top')
        url = popular_paper()[:10]
        ans = {'status': 200, 'item': 'GET', 'newspapers': newspapers, 'Url': url}
        return RestResponse(ans)


class TopNewsTopic(viewsets.ViewSet):
    def list(self, request):
        topic = request.GET.get('top')
        url = hot_news()[:10]
        ans = {'status': 200, 'item': 'GET', 'newspapers': topic, 'Url': url}
        return RestResponse(ans)


class LatestNews(viewsets.ViewSet):
    def list(self, request):
        topic = request.GET.get('top')
        url = top_news_title()
        ans = {'status': 200, 'item': 'GET', 'newspapers': topic, 'LatestNews Title And Publish Time': url}
        return RestResponse(ans)


class TopEducationNews(viewsets.ViewSet):
    def list(self, request):
        topic = request.GET.get('top')
        url = top_education_news()
        ans = {'status': 200, 'item': 'GET', 'newspapers': topic, 'Educational News Title': url}
        return RestResponse(ans)


class TopKoreanNews(viewsets.ViewSet):
    def list(self, request):
        topic = request.GET.get('top')
        link = top_news_korean()
        ans = {'status': 200, 'item': 'GET', 'newspapers': topic, 'Top News Title & Link': link}
        return RestResponse(ans)
