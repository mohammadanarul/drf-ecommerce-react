from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer

@api_view(['GET'])
def user_list_api(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def user_register_api(request):
    if request.method == 'POST':
        serializer =UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully Your Account created.'
            data['username'] = user.username
            data['email'] = user.email
            data['phone_number'] = user.phone_number
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST'])
def user_login_api(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    data = {}
    if user is not None:
        login(request, user)
        data['response'] = 'Successfully Login.'
        print(data)
        return Response(data)


