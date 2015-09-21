from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import pandas as pd, re
from django.core.serializers import serialize
from models import House


# Create your views here.
def index(request):
    return HttpResponse(listings_func(request.GET))


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})


def listings_func(request_dict):
    kwargs = {}
    request_dict = dict((k.lower(), v) for k, v in request_dict.iteritems())
    request_dict = {k: v for k, v in request_dict.iteritems() if re.match('^(max|min)_(price|bed|bath)$', k)}
    for k in request_dict:
        column = re.search("price|bed|bath", k).group(0)
        if column != 'price':
            column += "rooms"
        threshold = int(float(request_dict[k]))
        if re.search('min', k):
            kwargs['{0}__{1}'.format(column, 'gte')] = threshold
        else:
            kwargs['{0}__{1}'.format(column, 'lte')] = threshold
    print kwargs
    return serialize('geojson', House.objects.filter(**kwargs))
