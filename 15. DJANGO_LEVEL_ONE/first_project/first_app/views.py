from django.shortcuts import render
#from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    #my_dict = {'insert_me': "Now I am coming From first_app/views.py!"}
    return render(request, 'first_app/index.html', context=date_dict)
    # return HttpResponse("Hello World!")
