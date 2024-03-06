import random
from django.shortcuts import render


def generate_random_code(request):
    random_code = random.randint(1000, 9999)
    return render(request, 'random_code.html', {'random_code': random_code})
