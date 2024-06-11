# from django.http import JsonResponse, HttpResponse


# def home(request):
#     return HttpResponse("<h1>Welcome to the Calculator App</h1>")

# def add_numbers(request):
#     try:
#         # Get numbers from GET request
#         num1 = float(request.GET.get('num1', 0))
#         num2 = float(request.GET.get('num2', 0))
#         result = num1 + num2
#         return JsonResponse({'result': result})
#     except (TypeError, ValueError):
#         return JsonResponse({'error': 'Invalid input'}, status=400)




from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Calculator App</h1>")

def add_numbers(request):
    try:
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        result = num1 + num2
        return JsonResponse({'result': result})
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid input'}, status=400)

def subtract_numbers(request):
    try:
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        result = num1 - num2
        return JsonResponse({'result': result})
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid input'}, status=400)

def multiply_numbers(request):
    try:
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        result = num1 * num2
        return JsonResponse({'result': result})
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid input'}, status=400)

def divide_numbers(request):
    try:
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        if num2 == 0:
            return JsonResponse({'error': 'Division by zero'}, status=400)
        result = num1 / num2
        return JsonResponse({'result': result})
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid input'}, status=400)
