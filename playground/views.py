from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request - response
# request handler
# action
def calculate():
    x = 1
    y = 2
    return x
def say_hello(request):
    # pull data from db
    # transform data
    # send email
    #return HttpResponse('Hello world')(first used)
    # now render the response
    x = calculate()
    return render(request, 'hello.html', {'name': 'Vikaasni'}) # we can also add more param mapping string to dict

    

