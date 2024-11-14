from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsOwnerOrReadOnly, IsAdmin
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # IsAuthenticated требует, чтобы пользователь был аутентифицирован
    # permission_classes =[IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AdvertisementFilter
    ordering = ['created_at']

    def get_queryset(self):
        # получаем информацию о текущем пользователе
        current_user = self.request.user
        current_user_is_staff = self.request.user.is_staff
        # получаем информацию о статусах объявлений ["OPEN", "CLOSED"] для текущего пользователя
        if current_user_is_staff:
            queryset = Advertisement.objects.all()
            return queryset
        else:
            queryset_wo_draft = Advertisement.objects.all().filter(status__in =["OPEN","CLOSED"],creator=current_user)
            # получаем информацию о статусах объявлений "DRAFT" для текущего пользователя
            queryset_draft = Advertisement.objects.all().filter(status="DRAFT",creator=current_user)
            # возвращаем набор объявлений для текущего пользователя как объединение двух множеств
            return queryset_wo_draft | queryset_draft

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            is_admin = self.request.user.is_staff
            if is_admin:
                return [IsAdmin()]
            else:
                return [IsOwnerOrReadOnly()]
        return []
