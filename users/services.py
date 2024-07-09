from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response


def check_owner(self, request):
    user = self.get_object()
    if request.user == user:
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    else:
        raise PermissionDenied
