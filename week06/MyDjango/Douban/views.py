from django.shortcuts import render

# Create your views here.
from .models import T2
from django.db.models import Avg

def movies_short(request):
    ###  从models取数据传给template  ###
    shorts = T2.objects.all()

    condtions = {'n_star__gte': 3}
    threestarups = shorts.filter(**condtions)

    return render(request, 'result.html', locals())