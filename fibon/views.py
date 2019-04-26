from django.shortcuts import render
from django.views.generic import View
from fibon.models import ResultFibonacci
from fibon.forms import NumberForm
import math
from django.http import HttpResponse
import time,json
# Create your views here.

class FibonacciView(View):

    def get_fibo_number(self,num):
        ''' this is itreative approach  whose time complexity is O(n)'''
        if num < 2:
            return 1
        else:
            num_seq_1 = 1
            num_seq_2 = 1
            for i in range(2, num):
                temp = num_seq_1 + num_seq_2
                num_seq_1 = num_seq_2
                num_seq_2 = temp
            return num_seq_2
    def get_fibo_usinf_formula(self,num):
        ''' this approach is based on the mathematical formula  whose time complexity is O(1)'''
        result = (1 + math.sqrt(5))/2
        return round(pow(result,num)/math.sqrt(5))

    def get_fibo_by_dp(self,num):
        ''' this approach is based on dynamic programming whose time complexity is O(n)'''
        a=0
        b=1
        if num==0:
            return a
        for i in range(2,num+1):
            c = a + b
            a = b
            b = c
        return b



    def get(self,request):
        return render(request, 'home.html')

    def post(self,request):
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            number = int(number)
            if number:
                if not ResultFibonacci.objects.filter(number=number):
                    start_time = time.clock()
                    print start_time
                    result = self.get_fibo_by_dp(number)
                    result = str(result)
                    time_taken = time.clock() - start_time
                    fibonacci_object = ResultFibonacci(number=number,result=result,time_elapsed=time_taken)
                    fibonacci_object.save()
                    result = {
                        "number": number,
                        "result": result,
                        "time_elapsed": time_taken
                    }
                    #return HttpResponse(json.dumps(result), content_type='application/json', status=200)
                    return render(request,'result.html',{'result':result})
                else:
                    fibonacci_object = ResultFibonacci.objects.get(number=number)
                    result = {
                        "number":fibonacci_object.number,
                        "result":fibonacci_object.result,
                        "time_elapsed":fibonacci_object.time_elapsed
                    }
                    #return HttpResponse(json.dumps(result),content_type='application/json',status=200)
                    return render(request, 'result.html', {'result': result})


        else:
            form = NumberForm()
        return render(request, 'home.html')



