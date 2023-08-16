from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

customer_url = {
    "cars" : "Customer sees car",
    "drivers" : "Customer sees drivers",
    "mechanics" : "Customer sees mechanics"
}


def customer_view(request, customer) :
    
    try :
        text = customer_url[customer]
    except :
        return HttpResponseNotFound("Wrong Url!")
    
    return HttpResponse(text)



# Create your views here.
