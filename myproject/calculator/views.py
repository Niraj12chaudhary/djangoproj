# email_app/views.py

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# GET REQUEST VIEWS
def home(request):
    return HttpResponse("<h1>Welcome to the Calculator App</h1>")

def add_numbers_get(request):
    try:
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        result = num1 + num2
        return JsonResponse({'result': result})
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid input'}, status=400)

def subtract_numbers_get(request):
    try:
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        result = num1 - num2
        return JsonResponse({'result': result})
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid input'}, status=400)

def multiply_numbers_get(request):
    try:
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        result = num1 * num2
        return JsonResponse({'result': result})
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid input'}, status=400)

def divide_numbers_get(request):
    try:
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        if num2 == 0:
            return JsonResponse({'error': 'Division by zero'}, status=400)
        result = num1 / num2
        return JsonResponse({'result': result})
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid input'}, status=400)

# POST REQUEST VIEWS
@csrf_exempt
def add_numbers_post(request):
    return calculate_post(request, 'add')

@csrf_exempt
def subtract_numbers_post(request):
    return calculate_post(request, 'subtract')

@csrf_exempt
def multiply_numbers_post(request):
    return calculate_post(request, 'multiply')

@csrf_exempt
def divide_numbers_post(request):
    return calculate_post(request, 'divide')

def calculate_post(request, operation):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            num1 = float(data.get('num1'))
            num2 = float(data.get('num2'))

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    return JsonResponse({'error': 'Division by zero'}, status=400)
            else:
                return JsonResponse({'error': 'Invalid operation'}, status=400)

            return JsonResponse({'result': result})
        except (ValueError, TypeError, KeyError) as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
