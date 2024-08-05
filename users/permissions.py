from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Проверяет является ли пользователь владельцем объекта"""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsUser(permissions.BasePermission):
    """Проверяет является ли пользователь владельцем аккаунта"""
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsStaff(permissions.BasePermission):
    """Проверяет является ли пользователь персоналом сайта"""
    def has_permission(self, request, view):
        return request.user.is_staff is True
