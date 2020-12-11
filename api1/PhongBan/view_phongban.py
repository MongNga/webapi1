from rest_framework.response import Response
from rest_framework import status
from api1.PhongBan.model_phongban import User1
from rest_framework.decorators import api_view
from .serializer_phongban import getAllUserSerializers, userserializer
from django.db import connection


# Create your views here.


@api_view(['GET'])
def getuser_abcd(request):
    if request.method == 'GET':
        sql = "select * from TBM_USER "
        list_user = User1.objects.raw(sql)
        mydata = getAllUserSerializers(list_user, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
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
        sql = "insert into tbm_user(userid,username,pword,id) values("
        sql += "'" + userid + "','" + username + "','" + pword + "','" + str(pid) + "')"
        cursor = connection.cursor()
        cursor.execute(sql)

        # Return value
        return Response(data=userid, status=status.HTTP_200_OK)