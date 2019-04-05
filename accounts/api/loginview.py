from rest_auth.views import LoginView
from accounts.models import User
from .serializers import CustomLoginSerializer


class CustomLoginView(LoginView):

    # queryset = User.objects.all()
    # serializer_class = CustomLoginSerializer

    def get_response(self):
        response = super().get_response()
        data = {"message": "some message", "status": "success"}
        response.data.update(data)
        return response
