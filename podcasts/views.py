from rest_framework import viewsets, filters
from .models import Podcast
from .serializers import PodcastSerializer


class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'show_name', 'host', 'guest_speakers', 'description', 'tags']
    ordering_fields = ['created_at', 'year', 'season', 'episode_number']
    ordering = ['-season', '-episode_number', '-created_at']

    def get_queryset(self):
        """Filter by season, year, or host"""
        queryset = Podcast.objects.all()
        season = self.request.query_params.get('season', None)
        year = self.request.query_params.get('year', None)
        host = self.request.query_params.get('host', None)

        if season:
            queryset = queryset.filter(season=season)
        if year:
            queryset = queryset.filter(year=year)
        if host:
            queryset = queryset.filter(host__icontains=host)

        return queryset
