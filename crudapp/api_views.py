from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import *

@api_view(["GET", "POST"])
def getStudent(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    # students = { "name": "Meet Patel" , "email":"meet@gmail.com"}

    if request.method == "GET":
        return Response({
            "status" : 200,
            "message" : "Yes! Django REST Framework is runnning",
            "method_called" : f"{request.method}",
            "data" : serializer.data
        })
    elif request.method == "POST":
        return Response({
            "status" : 200,
            "message" : "Yes! Django REST Framework is runnning",
            "method_called" : f"{request.method}",
            "data" : serializer.data
        })

# def getStudent(request):
#     students = Student.objects.all()
#     students_python = list(students.values())
#     return JsonResponse({
#         'students' : students_python
#     })

@api_view(["POST"])
def postStudent(request):
    try:
        data=request.data
        print(data)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save() 
            return Response({
                "status" : 200,
                "message" : "Succesfully added student data",
                "method_called" : f"{request.method}",
                "data" : serializer.data
            })

        return Response({
                "status" : False,
                "message" : "Invalid Data",
                "method_called" : f"{request.method}",
                "data" : serializer.errors
            })

    except Exception as e:
        print(e)
    return Response({
            "status" : False,
            "message" : "Something Went wrong and student data is not saved",
            "method_called" : f"{request.method}",
        })

@api_view(["PATCH"])
def patchStudent(request):
    try:
        data=request.data
        print(data)

        if not data.get("id"):
            return Response({
                "status" : False,
                "message" : "Student ID is required",
                "method_called" : f"{request.method}",
                "data" : {}
            })
        
        student = Student.objects.get(id = data.get("id"))
        serializer = StudentSerializer(student ,data=data, partial=True)
        if serializer.is_valid():
            serializer.save() 
            return Response({
                "status" : 200,
                "message" : "Succesfully updated student data",
                "method_called" : f"{request.method}",
                "data" : serializer.data
            })

        return Response({
                "status" : False,
                "message" : "Invalid Data",
                "method_called" : f"{request.method}",
                "data" : serializer.errors
            })

    except Exception as e:
        print(e)
    return Response({
            "status" : False,
            "message" : "Something Went wrong and student data is not saved",
            "method_called" : f"{request.method}",
        })


class StudentVIEW(APIView):
    
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        # students = { "name": "Meet Patel" , "email":"meet@gmail.com"}
        return Response({
            "status" : 200,
            "message" : "Yes! Django REST Framework is runnning",
            "method_called" : f"{request.method}",
            "data" : serializer.data
        })
        
        
    def post(self, request):
        try:
            data=request.data
            print(data)
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    "status" : 200,
                    "message" : "Succesfully added student data",
                    "method_called" : f"{request.method}",
                    "data" : serializer.data
                })
            return Response({
                    "status" : False,
                    "message" : "Invalid Data",
                    "method_called" : f"{request.method}",
                    "data" : serializer.errors
                })
        except Exception as e:
            print(e)
        return Response({
                "status" : False,
                "message" : "Something Went wrong and student data is not saved",
                "method_called" : f"{request.method}",
            })
    
    def patch(self, request):
        try:
            data=request.data
            print(data)
            if not data.get("id"):
                return Response({
                    "status" : False,
                    "message" : "Student ID is required",
                    "method_called" : f"{request.method}",
                    "data" : {}
                })
            student = Student.objects.get(id = data.get("id"))
            serializer = StudentSerializer(student ,data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    "status" : 200,
                    "message" : "Succesfully updated student data",
                    "method_called" : f"{request.method}",
                    "data" : serializer.data
                })
            return Response({
                    "status" : False,
                    "message" : "Invalid Data",
                    "method_called" : f"{request.method}",
                    "data" : serializer.errors
                })
        except Exception as e:
            print(e)
        return Response({
                "status" : False,
                "message" : "Something Went wrong and student data is not saved",
                "method_called" : f"{request.method}",
            })
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=False, methods=['get'])
    def get_pass_status(self, request):
        is_passed = IsPassed.objects.all()
        serializer = IsPassedSerializer(is_passed, many=True)
        return Response({
            "status" : 200,
            "message" : "Yes! Django REST Framework is runnning",
            "method_called" : f"{request.method}",
            "data" : serializer.data
        })


    @action(detail=False, methods=['post'])
    def add_pass_status(self, request):
        try:
            data = request.data
            print(data)
            serializer = IsPassedSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status" : 200,
                    "message" : "Succesfully updated student passed status",
                    "method_called" : f"{request.method}",
                    "data" : serializer.data
                })
            return Response({
                    "status" : False,
                    "message" : "Invalid Data",
                    "method_called" : f"{request.method}",
                    "data" : serializer.errors
                })
        except Exception as e:
            print(e)
        return Response({
                "status" : False,
                "message" : "Something Went wrong and student data is not saved",
                "method_called" : f"{request.method}",
            })
        