from django.shortcuts import render
from .forms import TweetForm,UserRegistrationForm
from .models import Tweet
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q



# Create your views here.
def index(request):
    return render(request,'index.html')






def list_tweet(request):
    query = request.GET.get('q', '')
    tweet_type=request.GET.get('type','')
        
    tweets = Tweet.objects.all()
    if query:
        tweets = tweets.filter(title__icontains=query) | tweets.filter(text__icontains=query)

    # Filter by tweet type (if selected)
    if tweet_type:
        tweets = tweets.filter(type=tweet_type)

    # Pass the tweets, search query, and tweet types to the template
    return render(request, 'list_tweet.html', {
        'tweets': tweets,
        'search_query': query,
        'tweet_type': tweet_type,
        'tweet_types': Tweet.TWEET_CHOICES,
    })


@login_required
def tweet_detail(request, id):
    # Retrieve the tweet by its ID
    tweet = get_object_or_404(Tweet, id=id)
    
    # Pass the tweet object to the template
    return render(request, 'tweet_detail.html', {
        'tweet': tweet,
    })


@login_required
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
@login_required
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


@login_required
def delete_tweet(request,tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('list_tweet')
    return render(request,'tweet_delete.html',{'tweet':tweet})


def register(request):
    if request.method=='POST':
      form=UserRegistrationForm(request.POST)
      if form.is_valid():
          user=form.save(commit=False)
          user.set_password(form.cleaned_data['password1'])
          user.save()
          login(request,user)
          return redirect('list_tweet')

    else:
        form=UserRegistrationForm()
        
    return render(request,'registration/register.html',{'form':form})



    

