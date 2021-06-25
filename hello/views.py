from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'template1.html')

def run(request):
    w3 = int(request.GET['num'])
    w1 = w3*0.38
    w2 = w3*0.91
    w4 = w3*0.38
    w5 = w3*2.34
    w6 = w3*0.93
    w7 = w3*0.92
    w8 = w3*1.12

    return render(request, 'oeans.html', {'w1':'%0.2f'% w1, 'w2':'%0.2f'% w2, 'w3':'%0.2f'% w3,
                                          'w4':'%0.2f'% w4, 'w5':'%0.2f'% w5, 'w6':'%0.2f'% w6,
                                          'w7':'%0.2f'% w7, 'w8':'%0.2f'% w8})