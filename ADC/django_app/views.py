
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

data_values = []

@csrf_exempt
def data_input(request):
    global data_values
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            value = int(body.get('value', 765))
            data_values.append(value)
            if len(data_values) > 1000: 
                data_values.pop(0)
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "error", "message": "Invalid method"})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       