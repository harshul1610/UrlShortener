from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import UrlInputClass
# Create your views here.
@csrf_exempt
def index(request):
    if request.method=='POST':
        InputUrl = request.POST['InputUrl']
        #Algorithm to shorten url
        all_urls = UrlInputClass.objects.all()
        id = len(all_urls) + 1
        ShortenedKey = idToShortKey(id)
        model_object = UrlInputClass(InputUrl=InputUrl, ShortenedKey=ShortenedKey)
        try:
            model_object.save()
        except:
            return HttpResponse('already done')
        return HttpResponse(model_object.__repr__())
    return render(request, 'index.html')

def idToShortKey(id):
    map = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    shortkey = []
    while id:
        shortkey.append(map[id%62])
        id=id/62
    return ''.join(shortkey)

def redirectview(request,shortkey):
    id = 0
    for i in shortkey:
        if ord('a')<=ord(i) and ord(i)<=ord('z'):
            id=(id*62+ord(i))-ord('a')
        elif ord('A')<=ord(i) and ord(i)<=ord('Z'):
            id=(id*62+ord(i)+26)-ord('A')
        elif int('0')<=int(i) and int(i)<=int('9'):
            id=(id*62+ord(i)+52)-int('0')

    fullurlobj = UrlInputClass.objects.get(pk=id)
    return redirect(to=fullurlobj.InputUrl)
    #return HttpResponse(id)

