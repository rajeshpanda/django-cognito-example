from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.all()[0].name == "ADMIN"


class IsConsultant(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.all()[0].name == "CONSULTANT"


class IsBusiness(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.all()[0].name == "BUSINESS"
