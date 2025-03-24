from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    """
    Custom permission to allow only superusers to access the view.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsDoctorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_doctor or user.is_admin)