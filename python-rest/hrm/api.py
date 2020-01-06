from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class UserAuthentication(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception= True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response(token.key)

class UserList(APIView):
    def get(self,request):
        model = Users.objects.all()
        serializer = UsersSerializer(model,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get(self,request,employee_id):
        try:
            model = Users.objects.get(id = employee_id)
        except Users.DoesNotExist:
            return Response("User Not Found",status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,employee_id):
        try:
            model = Users.objects.get(id = employee_id)
        except Users.DoesNotExist:
            return Response("User Not Found",status=status.HTTP_404_NOT_FOUND)

        serializer = UsersSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,employee_id):
        try:
            model = Users.objects.get(id = employee_id)
        except Users.DoesNotExist:
            model = None
            
        if model == None:
            return Response("User Not Found",status=status.HTTP_404_NOT_FOUND)
        model.delete()
        return Response('User Deleted',status=status.HTTP_404_NOT_FOUND)
