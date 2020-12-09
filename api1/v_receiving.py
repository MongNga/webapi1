from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection

# Create your views here.

class getUserAPIView(APIView):

     def dictfetchall(cursor):
         columns = [col[0] for col in cursor.description]
         return [
             dict(zip(columns, row))
             for row in cursor.fetchall()
         ]

     def get(self, request):
         cursor = connection.cursor()
         sql = "select * from tbt_boxdata where dnno = 'B0918100132' "
         data = getUserAPIView.dictfetchall(cursor.execute(sql))
         return Response(data=data, status=status.HTTP_200_OK)
