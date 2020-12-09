# from django.shortcuts import render
# from rest_framework.authentication import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework.decorators import api_view
from .serializers import getAllUserSerializers, userserializer
from django.db import connection


# Create your views here.

# @api_view(['GET','POST'])
# def get_user(request):
#     if request.method == 'GET':
#         cursor = connection.cursor()
#         sql = "select * from TBM_USER "
#         data = Json(cursor.execute(sql))
#         # return Response(data=data, status=status.None)
#         return Response({"message": "Hello, world!"})


@api_view(['GET'])
def getuser_abc(request):
    if request.method == 'GET':
        sql = "select * from TBM_USER "
        list_user = User.objects.raw(sql)
        mydata = getAllUserSerializers(list_user, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def postuser(request):
    if request.method == 'POST':
        mydata = userserializer(data=request.data)
        # print(request.data)
        if not mydata.is_valid():
            return Response(data="N hap gia tri", status=status.HTTP_400_BAD_REQUEST)
        userid = mydata.data['userid']
        username = mydata.data['username']
        pword = mydata.data['pword']
        pid = mydata.data['id']
        # print("Mong Nga" + pid)
        # cs = User.objects.create(userid=userid, username=username, pword=pword, id=pid)
        # return Response(data=cs.id, status=status.HTTP_200_OK)
        sql1 = "insert into tbm_user(userid,username,pword,id) values("
        sql2 = "'" + userid + "','" + username + "','" + pword + "','" + str(pid) + "')"
        sql = sql1 + sql2
        # print(sql)
        cursor = connection.cursor()
        # print(sql)
        cursor.execute(sql)

        # Return value
        return Response(data=userid, status=status.HTTP_200_OK)


class getAllUserAPIView(APIView):

    # def get(self, request):
    #     list_user = User.objects.all()
    #     mydata = getAllUserSerializers(list_user, many=True)
    #     return Response(data=mydata.data, status=status.HTTP_200_OK)

    def get(self, request):
        sql = "select * from TBM_USER "
        list_user = User.objects.raw(sql)
        mydata = getAllUserSerializers(list_user, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

    # def get(self, request):
    #     # print(get_user_model())
    #     cursor = connection.cursor()
    #     sql = "select * from TBM_USER "
    #     data = Json(cursor.execute(sql))
    #     return Response(data=data, status=status.HTTP_200_OK)

#
#     @APIView(['GET'])
#     def get_abc(request):
#         if request.method == 'GET':
#             cursor = connection.cursor()
#             sql = "select * from TBM_USER "
#             data = Json(cursor.execute(sql))
#             return Response(data=data, status=status.HTTP_200_OK)


# def post(self, request):
#     mydata = userSerializer(data=request.data)
#     # print(request.data)
#     if not mydata.is_valid():
#         return Response(data="N hap gia tri", status=status.HTTP_400_BAD_REQUEST)
#     userid = mydata.data['userid']
#     username = mydata.data['username']
#     pword = mydata.data['pword']
#     sql = "insert into tbm_user(userid,username,pword) values('"
#     sql += userid + "','" + username + "'," + "'" + pword + "')"
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     # Return value
#     sql = "select * from TBM_USER "
#     data = Json(cursor.execute(sql))
#     return Response(data=data, status=status.HTTP_200_OK)
#     return Response(data="OK", status=status.HTTP_200_OK)
