from django.shortcuts import render
from .models import images
from django.http import JsonResponse
from .chat_bot import medical_chatbot

def index(request):
    im=images.objects.filter(name='avatar')
    h={'avatar':im}
    return render(request,'chatbot/index.html',h)

def reply(request):
    if request.method == 'GET':
        query=request.GET.get('message')
        query=query.lower()
        try:
            bot_response=medical_chatbot.chatbot_reply(query=query)
        except Exception:
            bot_response='Sorry but i am unable to understand what you are saying....'       
        return JsonResponse({'message':bot_response})
    else:
        return JsonResponse({'error':'invalid request meathod.'})


