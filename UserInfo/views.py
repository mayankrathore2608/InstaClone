from UserInfo.models import UserCred
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import UserCred


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserCred.objects.all()
    serializer_class = UserSerializer
