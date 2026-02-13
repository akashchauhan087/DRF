from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
import traceback as tb

@api_view(['GET'])
def home(request):
    return Response({'status':'success', 'statusCode':status.HTTP_200_OK, 'message':'Welcome to the Homepage...'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_students(request):
    student_data = Student.objects.all()
    serializer = StudentSerializer(student_data, many=True)
    return Response({'status':'success', 'statusCode':status.HTTP_200_OK, 'payload':serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_student_details(request):
    if request.method == 'POST':
        # print(request.data)
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':'failure', 'statusCode': status.HTTP_400_BAD_REQUEST, 'message':'Data shared is not vaild', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'status':'success', 'statusCode':status.HTTP_201_CREATED, 'message':'Details inserted successfully...', 'data':request.data}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def student_details(request, id):
    try:
        if request.method == 'GET':
            obj_student = Student.objects.get(pk=id)
            if not obj_student:
                return Response({'status':'failure', 'statusCode':status.HTTP_404_NOT_FOUND, 'message':'Student details not found...'}, status=status.HTTP_404_NOT_FOUND)
            serializer = StudentSerializer(obj_student)
            return Response({'status':'success', 'statusCode':status.HTTP_200_OK, 'payload':serializer.data}, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            obj_student = Student.objects.filter(pk=id).first()
            serializer = StudentSerializer(obj_student, data=request.data)
            if not serializer.is_valid():
                return Response({'status':'failure', 'statusCode':status.HTTP_400_BAD_REQUEST, 'message':'Data shared is not vaild', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'status':'success', 'statusCode':status.HTTP_200_OK, 'message':'Details updated successfully...'}, status=status.HTTP_200_OK)
        
        elif request.method == 'PATCH':
            obj_student = Student.objects.filter(pk=id).first()
            serializer = StudentSerializer(obj_student, data=request.data)
            if not serializer.is_valid():
                return Response({'status':'failure', 'statusCode':status.HTTP_404_NOT_FOUND, 'message':'Student details not found...'}, status=status.HTTP_404_NOT_FOUND)
            serializer.save()
            return Response({'status':'success', 'statusCode':status.HTTP_200_OK, 'message':'Details updated successfully...'}, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            obj_student = Student.objects.filter(id=id).first()
            if not obj_student:
                return Response({'status':'failure', 'statusCode':status.HTTP_404_NOT_FOUND, 'message':'Student details not found...'}, status=status.HTTP_404_NOT_FOUND)
            obj_student.delete()
            return Response({'status':'success', 'statusCode':status.HTTP_200_OK, 'message':'Details deleted successfully...'}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'status':'failure', 'statusCode':status.HTTP_500_INTERNAL_SERVER_ERROR, 'message':'Something went wrong...', 'error':tb.format_exc()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
