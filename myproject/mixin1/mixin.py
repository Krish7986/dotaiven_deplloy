from django.http  import HttpResponse
class mixinreponse:
    def fun(self,request):
        return HttpResponse("hello everyone")