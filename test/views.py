from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def get_object_or_404(stops, name=""):
    if name in stops:
        return stops[name]
    else:
        return None


def home(request):
    return render_to_response(
        'index.html',
        {
            'stop_list': [
                {
                    'stopId':'1',
                    'name':'main street',
                },
                {
                    'stopId':'2',
                    'name':'wall street',
                },
            ]
        
        },
        context_instance=RequestContext(request)
    )
