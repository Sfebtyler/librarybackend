from rest_framework import viewsets
from app.serializers import *
from rest_framework import permissions, status
from rest_framework.decorators import list_route
from rest_framework.response import Response



class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-check_in')
    serializer_class = BooksSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}

    def get_queryset(self):
        if self.action == 'available':
            return super().get_queryset().filter(checked_out = None)
        return super().get_queryset()

    @list_route(['GET'])
    def available(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = []


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        return Response(status=400)

    @list_route(methods=['GET'], permission_classes=[])
    def current_user(self, request, *args, **kwargs):
        if self.request.user:
            return Response(UserSerializer(self.request.user, context={'request': request}).data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Not logged in!'}, status=status.HTTP_401_UNAUTHORIZED)

    @list_route(methods=['POST'], permission_classes=[])
    def create_user(self, request):
        UserSerializer.create_user(self, request)
        return Response(User)
