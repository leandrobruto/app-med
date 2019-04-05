from rest_framework.viewsets import ModelViewSet
from teste.models import Album
from .serializers import AlbumSerializer


class TesteViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
