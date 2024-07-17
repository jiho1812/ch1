from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
import json

@csrf_exempt
@require_POST
def add_points(request):
    try:
        data = json.loads(request.body)
        nickname = data['nickname']
        points_to_add = data['points']

        user, created = UserProfile.objects.get_or_create(nickname=nickname)
        user.points += points_to_add
        user.save()

        response = {
            'nickname': user.nickname,
            'points': user.points
        }
        return JsonResponse(response, status=200)

    except (KeyError, ValueError) as e:
        return JsonResponse({'error': str(e)}, status=400)
