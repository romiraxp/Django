from rest_framework.permissions import BasePermission
class IsOwnerOrReadOnly(BasePermission):
    # has_permission: имеет ли пользователь право на работу с ресурсом в целом, по умолчанию возвращает True
    # def has_permission(self, request, view):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    # has_object_permission: данный метод проверяет права на конкретный объект.
    # Будем проверять пользователя из запроса с пользователем, который создал объект
    def has_object_permission(self, request, view, obj):
        # будем возвращать true или false в случае если пользователь из запроса совпадает с пользователем объекта
        if request.method == "GET":
            return True
        return request.user == obj.creator # сравниваем с obj.creator, которое является в свою очерель полем в модели

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return request.user.is_staff
