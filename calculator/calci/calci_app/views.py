from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit(request):
    q = request.GET.get('query')
    mydict = {}
    if not q:
        
        return render(request, 'index.html',context=mydict)

    try:
        ans = eval(q)
        mydict = {
            'q' : q,
            'ans' : ans,
            'error' : False
        }
        return render(request, 'index.html', context=mydict)
    except:
        mydict = {
            'error' : True
        }
        return render(request, 'index.html', context=mydict)
        