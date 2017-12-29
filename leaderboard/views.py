from django.shortcuts import render, get_object_or_404,redirect
from .models import Scorecard
from .forms import Enter_Score
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout 
# Create your views here.



def score_list(request):
    order_by = request.GET.get('order_by', 'score')
    scores = Scorecard.objects.all().order_by(order_by).reverse()
    dataFromModel = {
        'scores':scores
    }
    return render(request , 'leaderboard/score_list.html',dataFromModel)


def score_detail(request,pk):
    score_view = get_object_or_404(Scorecard,pk=pk)
    return render(request , 'leaderboard/score_detail.html' , { 'score_view':score_view })


def new_score(request):
    if request.method == 'POST':
        form = Enter_Score(request.POST)
        print('form')
        print(form)
        if form.is_valid():
            post = form.save(commit = False)
            post.creator = request.user
            post.save()
            return redirect('score_detail',pk = post.pk )
    else:
        form = Enter_Score()
        
        return render(request, 'leaderboard/score_new.html', {'form': form})


def score_edit(request,pk):
    post = get_object_or_404(Scorecard , pk=pk)
    if request.method == "POST":
        form = Enter_Score(request.POST , instance = post)
        if form.is_valid() and request.user == post.creator:
            post = form.save(commit = False)
            post.save()
            return redirect('score_detail' , pk = post.pk )
        else:
            message = "Sorry,you dont have permission to modify this post"
            return render(request, 'leaderboard/request_failed.html', {'message': message})
        
    else:
        form = Enter_Score(instance=post)
        return render(request , 'leaderboard/score_new.html' , {'form':form})


def score_delete(request, pk):
    check = Scorecard.objects.get(serialNo=pk)
    if check.creator == request.user:
        post = Scorecard.objects.get(serialNo = pk).delete()
        return redirect('score_list')
    else:
        message = "Sorry,you dont have permission to modify this post"
        return render(request, 'leaderboard/request_failed.html', {'message': message})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            obj = form.save()
            user = authenticate(username = username , password = password)
            login(request,user)
            return redirect('score_list')
    else:
        form = UserCreationForm()
    return render(request , 'leaderboard/signup.html' , { 'form':form })


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username ,password = password)
        if user is not None:
            login(request, user)
            return redirect('score_list')
    else:
        form = AuthenticationForm()
    return render(request , 'leaderboard/signin.html' , {'form': form})


def signout(request):
    logout(request)
    return render(request,'leaderboard/signout.html')



