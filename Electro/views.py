from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from .models import Electro
from .serializer import ElectroSerializer


class ElectroListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Electro.objects.all()
    serializer_class = ElectroSerializer


class ElectroDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Electro.objects.all()
    serializer_class = ElectroSerializer
