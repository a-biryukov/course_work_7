from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """Проверяет является ли пользователь владельцем аккаунта"""
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
