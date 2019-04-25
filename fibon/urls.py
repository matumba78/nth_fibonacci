from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from fibon.views import FibonacciView

urlpatterns=[

    url(r'^home/',csrf_exempt(FibonacciView.as_view()),name='home-view'),
    url(r'^fibo-number/',csrf_exempt(FibonacciView.as_view()),name='result-view'),

]