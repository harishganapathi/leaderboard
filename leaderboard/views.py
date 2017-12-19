from django.shortcuts import render
from .models import Scorecard
# Create your views here.
def score_list(request):
    scores = Scorecard.objects.all()
    dataFromModel = {
        'scores':scores
    }
    return render(request , 'leaderboard/score_list.html',dataFromModel )