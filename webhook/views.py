from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from library.df_response_lib import *
import json
from .Engine.phone import *

# Create your views here.

def home(request):
    return render(request, 'webhook/home.html')

@csrf_exempt
def webhook(request):
    # build a request object 
    req = json.loads(request.body) 
    # get action from json 
    action = req.get('queryResult').get('action') 
    if action == "dept_head":
        result = req.get("queryResult")
        parameters = result.get("parameters")
        dept_head = parameters.get("dept-head")
        
        speech = "Department Head of \n" + dept_head + " : " + str(phone[dept_head])
        fulfillmentText = {'fulfillmentText': speech} 
        aog = actions_on_google_response()
        aog_sr = aog.simple_response([ 
            [fulfillmentText, fulfillmentText, False]
        ])
        #create suggestion chips
        aog_sc = aog.suggestion_chips(["suggestion1", "suggestion2"])
        ff_response = fulfillment_response()
        ff_text = ff_response.fulfillment_text(fulfillmentText) 
        ff_messages = ff_response.fulfillment_messages([aog_sr, aog_sc])
        reply = ff_response.main_response(ff_text, ff_messages)
    # return a fulfillment message 
    
    # return response 
    return JsonResponse(fulfillmentText, safe=False)