from django.shortcuts import render
from .forms import TweetForm
from .models import Tweet
from django.shortcuts import get_object_or_404,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')



def list_tweet(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'list_tweet.html',{'tweets':tweets})



def create_tweet(request):
    if request.method=='POST':
       form=TweetForm(request.POST, request.FILES)
       if form.is_valid():
           unsave_tweet=form.save(commit=False)   #dcommit false means dont save in db just store
           unsave_tweet.user=request.user
           unsave_tweet.save()
           return redirect('list_tweet')
    else: 
       form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})

#edit garni bela instance dinu parxa to know we are editing the previous tweet
def edit_tweet(request,tweet_id):
    prev_tweet=get_object_or_404(Tweet, pk=tweet_id,user=request.user)
    if request.method=='POST':
       form=TweetForm(request.POST, request.FILES, instance=prev_tweet)
       if form.is_valid():
           prev_tweet=form.save(commit=False)
           prev_tweet.user=request.user
           prev_tweet.save()
           return redirect('list_tweet')
      
    else:
        form=TweetForm(instance=prev_tweet)
    return render(request,'tweet_form.html',{'form':form})

def delete_tweet(request,tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('list_tweet')
    return render(request,'tweet_delete.html',{'tweet':tweet})





    

