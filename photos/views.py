from rest_framework import viewsets, filters
from .models import Photo, PhotoGallery
from .serializers import PhotoSerializer, PhotoGallerySerializer


class PhotoGalleryViewSet(viewsets.ModelViewSet):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'year']
    ordering = ['-created_at']


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'photographer', 'location', 'tags', 'caption']
    ordering_fields = ['created_at', 'year']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by gallery, category, featured status"""
        queryset = Photo.objects.all()
        gallery_id = self.request.query_params.get('gallery', None)
        category = self.request.query_params.get('category', None)
        featured = self.request.query_params.get('featured', None)

        if gallery_id:
            queryset = queryset.filter(gallery_id=gallery_id)
        if category:
            queryset = queryset.filter(category=category)
        if featured:
            queryset = queryset.filter(featured=featured.lower() == 'true')

        return queryset
