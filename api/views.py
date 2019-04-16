from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response as RestResponse

from .google_news import top_news_title, top_education_news
from .popular_newspaper import popular_paper, hot_news
from .serializers import UserSerializer, GroupSerializer
from .korean_news import bbc_korean_news, world_korean_news, google_korean_news, korean_sports_news
from .dailystar_top_news import daily_star_news
from .bangla_bbc_news import bangla_bbc_news
from .japanese_news import bbc_japan_news, world_latest_news, japanese_sports_news
from .english_news import world_news, english_sports_news
from .sports_news import sports_news


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
        link = bbc_korean_news()
        ans = {'status': 200, 'item': 'GET', 'newspapers': topic, 'Top News Title & Link': link}
        return RestResponse(ans)


class DailyStarTopNews(viewsets.ViewSet):
    def list(self, request):
        topic = request.GET.get('top')
        link = daily_star_news()
        ans = {'status': 200, 'item': 'GET', 'newspapers': topic, 'Top News Title & Link': link}
        return RestResponse(ans)


class BanglaBccNews(viewsets.ViewSet):
    def list(self, request):
        topic = request.GET.get('top')
        link = bangla_bbc_news()
        ans = {'status': 200, 'item': 'GET', 'newspapers': topic, 'Top News Title & Link': link}
        return RestResponse(ans)


class JapanBccNews(viewsets.ViewSet):
    def list(self, request):
        topic = request.GET.get('top')
        link = bbc_japan_news()
        ans = {'status': 200, 'item': 'GET', 'newspapers': topic, 'Top News Title & Link': link}
        return RestResponse(ans)


class SportsNews(viewsets.ViewSet):
    def list(self, request):
        topic = request.GET.get('top')
        link = sports_news()
        ans = {'status': 200, 'item': 'GET', 'newspapers': topic, 'Top News Title & Link': link}
        return RestResponse(ans)


class AllNews(viewsets.ViewSet):
    def list(self, request):
        language = request.GET.get('lan')
        newspaper = request.GET.get('paper')

        if language == 'ja':
            if newspaper == 'world':
                link = world_latest_news()
                ans = {'status': 200, 'item': 'GET', 'language': language, 'newspaper': newspaper, 'Top News Title': link}
                return RestResponse(ans)

            if newspaper == 'google':
                link = google_korean_news()
                ans = {'status': 200, 'item': 'GET', 'language': language, 'newspaper': newspaper, 'Top News Title': link}
                return RestResponse(ans)

            if newspaper == 'bbc':
                link = bbc_japan_news()
                ans = {'status': 200, 'item': 'GET', 'language': language, 'newspaper': newspaper, 'Top News Title': link}
                return RestResponse(ans)

            if newspaper == 'sports':
                link = japanese_sports_news()
                ans = {'status': 200, 'item': 'GET', 'language': language, 'newspaper': newspaper, 'Top News Title': link}
                return RestResponse(ans)

            else:
                ans = {'status': 201, 'item': 'GET', 'newspapers': language, 'Top News Title ': "Not valid"}
                return RestResponse(ans)

        if language == 'ko':
            if newspaper == 'world':
                link = world_korean_news()
                ans = {'status': 200, 'item': 'GET', 'language': language, 'newspaper': newspaper, 'Top News Title': link}
                return RestResponse(ans)

            if newspaper == 'google':
                link = google_korean_news()
                ans = {'status': 200, 'item': 'GET', 'language': language, 'newspaper': newspaper, 'Top News Title': link}
                return RestResponse(ans)

            if newspaper == 'bbc':
                link = bbc_korean_news()
                ans = {'status': 200, 'item': 'GET', 'language': language, 'newspaper': newspaper, 'Top News Title': link}
                return RestResponse(ans)

            if newspaper == 'sports':
                link = korean_sports_news()
                ans = {'status': 200, 'item': 'GET', 'language': language, 'newspaper': newspaper, 'Top News Title': link}
                return RestResponse(ans)

            else:
                ans = {'status': 201, 'item': 'GET', 'newspapers': language, 'Top News Title ': "Not valid"}
                return RestResponse(ans)

        if language == 'bn':
            link = bangla_bbc_news()
            ans = {'status': 200, 'item': 'GET', 'newspapers': language, 'Top News Title & Link': link}
            return RestResponse(ans)

        if language == 'en':
            if newspaper == 'world':
                link = world_news()
                titles = link
                ans = {'status': 200, 'item': 'GET', 'newspapers': language, 'Top News Title & Link': titles}
                return RestResponse(ans)

            if newspaper == 'sports':
                link = english_sports_news()
                ans = {'status': 200, 'item': 'GET', 'language': language, 'newspaper': newspaper, 'Top News Title': link}
                return RestResponse(ans)

        else:
            ans = {'status': 200, 'item': 'GET', 'newspapers': language, 'Top News Title & Link': 'Not valid'}
            return RestResponse(ans)
