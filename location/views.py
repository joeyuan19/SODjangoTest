from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def get_object_or_404(stops, name=""):
    if name in stops:
        return stops[name]
    else:
        return None


def route(request):
    stops = {
        "1":{
            "name":"main street",
            "location":"50,50",
        },
        "2":{
            "name":"wall street",
            "location":"12,10",
        },
    }
    
    stop1 = get_object_or_404(stops, name=request.POST.get("stop1name","default_value"))
    stop2 = get_object_or_404(stops, name=request.POST.get("stop2name","default_value"))
    
    print(request.method)
    print(request.POST.dict())
    print(request.GET.dict())
    print(request.body)
    return render_to_response(
        'stop_selection.html',
        {
           "stop1":stop1,
           "stop2":stop2,
        },
        context_instance=RequestContext(request)
    )


