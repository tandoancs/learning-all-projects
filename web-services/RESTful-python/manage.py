from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def my_api_view(request):
    if request.method == "GET":
        data = {"message": "Hello from Django API"}
        return JsonResponse(data)
