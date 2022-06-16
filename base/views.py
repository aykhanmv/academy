from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
from academy.settings import env
import random
import time
import json

from .models import RoomMember

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def getToken(request):
    appId ='3f713793fc3b451d97b1859f46369a01'
    appCertificate ='9fa218ba6b1445cc981760edf6a8602a'
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expireationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expireationTimeInSeconds
    role = 1
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token, 'uid': uid}, safe=False)

def lobby(request):
    return render (request, 'base/lobby.html')

def room(request):
    return render (request, 'base/room.html')

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)

    member, created = RoomMember.objects.get_or_create(
        name = data['name'],
        uid = data['UID'],
        room_name = data['room_name']
    )
    return JsonResponse({'name':data['name']}, safe=False)

def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid = uid,
        room_name = room_name,
    )

    name = member.name
    return JsonResponse({'name':member.name}, safe=False)


@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    print(data['name'], data['UID'], data['room_name'])
    try:
        member = RoomMember.objects.get(
            name=data['name']
        )
        member.delete()
        print("Record deleted successfully!")
    except:
        print("Record doesn't exists")
    return JsonResponse('Member deleted', safe=False)