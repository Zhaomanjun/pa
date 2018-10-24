from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse, FileResponse
from django.template import loader
from .models import Blog

# Create your views here.
def showtongtong(request, tongId):
    t = loader.get_template('tongzhi.html')
    tong = Blog.objects.get(id=tongId)
    context = {'tongzhi': tong}
    html = t.render(context)
    return HttpResponse(html)

def showList(request):
    t = loader.get_template('tong_list.html')
    tongs = Blog.objects.all()
    context = {'tongzhis': tongs}
    html = t.render(context)
    return HttpResponse(html)
