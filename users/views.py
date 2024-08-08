from rest_framework.viewsets import ModelViewSet

from habits.paginators import CustomPaginator
from users.models import User
from users.permissions import IsUser
from users.serializer import UserSerializer, UserListSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPaginator

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'retrieve']:
            self.permission_classes = [IsUser]

        return super().get_permissions()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer

        return super().get_serializer_class()