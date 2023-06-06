from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    allowed_user_roles = ('admin', )

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if (
                request.user.role in self.allowed_user_roles
                or request.user.is_superuser
            ):
                return True
        return False


class IsModerator(BasePermission):
    allowed_user_roles = ('moderator', )

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role in self.allowed_user_roles:
                return True
        return False


class IsUser(BasePermission):
    allowed_user_roles = ('user', )

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role in self.allowed_user_roles:
                return True
        return False


class IsAdminOrReadOnly(BasePermission):
    allowed_user_roles = ('admin', )

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated 
            and request.user.role in self.allowed_user_roles
        )


class AdminOrModeratorIsAuthorPermission(BasePermission):
    allowed_user_roles = ('admin', 'moderator', )

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
            or request.user.role in self.allowed_user_roles
        )
