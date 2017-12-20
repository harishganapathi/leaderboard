from django.shortcuts import render, get_object_or_404,redirect
from .models import Scorecard
from .forms import Enter_Score
# Create your views here.
def score_list(request):
    scores = Scorecard.objects.all()
    dataFromModel = {
        'scores':scores
    }
    return render(request , 'leaderboard/score_list.html',dataFromModel )

def score_detail(request,pk):
    #score = Scorecard.objects.get(sno)
    score_view = get_object_or_404(Scorecard,pk=pk)
    #score_view = get_object_or_404(Scorecard , serialNo = sno)
    return render(request , 'leaderboard/score_detail.html' , { 'score_view':score_view })

def new_score(request):
    if request.method == 'POST':
        form = Enter_Score(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('score_detail',pk = post.pk )
    else:
        form = Enter_Score()
        return render(request, 'leaderboard/score_new.html', {'form': form})

def score_edit(request,pk):
    post = get_object_or_404(Scorecard , pk=pk)
    if request.method == "POST":
        form = Enter_Score(request.POST , instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('score_detail' , pk = post.pk )
    else:
        form = Enter_Score(instance=post)
        return render(request , 'leaderboard/score_new.html' , {'form':form})


def score_delete(request, pk):
    post = Scorecard.objects.get(serialNo = pk).delete()
    return redirect('score_list')

