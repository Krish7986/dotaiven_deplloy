from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("hello")

users = [
    {
        "id": 1,
        "name": "Hari Krishna",
        "age": 23,
        "gender": "Male",
        "email": "hari@gmail.com",
        "phone": "9876543210",
        "city": "Hyderabad"
    },
    {
        "id": 2,
        "name": "Ananya Sharma",
        "age": 22,
        "gender": "Female",
        "email": "ananya@gmail.com",
        "phone": "9876543211",
        "city": "Bangalore"
    },
    {
        "id": 3,
        "name": "Rahul Verma",
        "age": 28,
        "gender": "Male",
        "email": "rahul@gmail.com",
        "phone": "9876543212",
        "city": "Delhi"
    },
    {
        "id": 4,
        "name": "Sneha Reddy",
        "age": 24,
        "gender": "Female",
        "email": "sneha@gmail.com",
        "phone": "9876543213",
        "city": "Chennai"
    },
    {
        "id": 5,
        "name": "Amit Kumar",
        "age": 30,
        "gender": "Male",
        "email": "amit@gmail.com",
        "phone": "9876543214",
        "city": "Pune"
    },
    {
        "id": 6,
        "name": "Priya Singh",
        "age": 26,
        "gender": "Female",
        "email": "priya@gmail.com",
        "phone": "9876543215",
        "city": "Mumbai"
    },
    {
        "id": 7,
        "name": "Rohit Mehta",
        "age": 29,
        "gender": "Male",
        "email": "rohit@gmail.com",
        "phone": "9876543216",
        "city": "Ahmedabad"
    },
    {
        "id": 8,
        "name": "Kavya Nair",
        "age": 21,
        "gender": "Female",
        "email": "kavya@gmail.com",
        "phone": "9876543217",
        "city": "Kochi"
    },
    {
        "id": 9,
        "name": "Suresh Patel",
        "age": 35,
        "gender": "Male",
        "email": "suresh@gmail.com",
        "phone": "9876543218",
        "city": "Surat"
    },
    {
        "id": 10,
        "name": "Neha Joshi",
        "age": 27,
        "gender": "Female",
        "email": "neha@gmail.com",
        "phone": "9876543219",
        "city": "Jaipur"
    }
]
@csrf_exempt
def product(request,id):
    for i in users:
        print(i["name"])
        if i["id"] == id:
            return HttpResponse({"stus":"data showed","data":i},status = 200)
        
    return HttpResponse({"status":"error"},status = 400)
    
