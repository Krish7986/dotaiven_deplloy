from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import uuid
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .supabase_client import supabase

def re(request):
    return JsonResponse({"data":"the data shown successfully"})

# Create your views here.
@csrf_exempt
def user_profile(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        profile_pic = request.FILES.get("profile_pic")
        ext = profile_pic.name.split(".")[-1]
        file_name = f"{uuid.uuid4()}.{ext}"
        file_path = f"user/{file_name}"
        print("filename",file_name)
        print("path",file_path)

        supabase.storage.from_("first-bucket").upload(
        file_path,
        profile_pic.read(),
        {"content-type": profile_pic.content_type}
)


        public_url = supabase.storage.from_("profile_pic").get_public_url(file_path)

        user = User.objects.create(
            name = name,
            email = email,
            gender = gender,
            profile_pic = public_url
            )
        return JsonResponse({"status":"public url inserted"},status = 200)




    return JsonResponse({"status":"error"},status = 400)
        # if not all([name,email,gender,profile_pic]):
        #     return JsonResponse({"status":"all fields requried"},status = 400)
