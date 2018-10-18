from django.shortcuts import render, redirect,get_object_or_404,reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from annoying.decorators import ajax_request
from .forms import PhotoUploadModelForm,DesignForm,VoteForm,UsabilityForm,ContentForm
from django.contrib.auth.decorators import login_required

from .models import PostedSite,Comment,UsabilityRating,DesignRating,ContentRating
from userauth.models import User,Profile
from rest_framework import generics
from .serializers import PostedSiteSerializer

def home(request):
    posts= PostedSite.objects.all(),

    # commentform= CommentForm()
    
    return render(request, 'index.html', locals())

class PostListView(ListView):
    model=PostedSite

    template_name= 'awards/post_list.html' # <app>/<model>_<view_type>.html
    
    context_object_name = 'posts'
    ordering = ['-time_created']




class PostCreateView(CreateView):
    form_class = PhotoUploadModelForm
    template_name = 'awards/create_post.html'
 
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.user_profile= self.request.user.profile
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = PostedSite
    template_name= 'awards/post_detail.html' # <app>/<model>_<view_type>.html


# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = PostedSite
#     fields = ['title', 'content']

# class create_comment(CreateView):
#     model=Comment
#     template_name= 'awards/image_list.html' # <app>/<model>_<view_type>.html
    
#     context_object_name = 'comments'
#     ordering = ['-posted_on']

def signout(request):
    logout(request)
    return redirect('login')



def add_comment(request,post_id):
    post = get_object_or_404(PostedSite, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user

            comment.post = post
            comment.save()
    return redirect('home')


# @login_required(login_url='/accounts/login/')
# def search_results(request):
#     if 'searchItem' in request.GET and request.GET["searchItem"]:
#         search_term = request.GET.get("searchItem")
#         searched_user = Profile.search_by_username(search_term)
#         # user = User.objects.get(username=searched_user)
#         # user_images = Profile.objects.get(user=searched_user)
#         message = f"{search_term}"
#         context = {
#             'message': message,
#             'searched_user': searched_user
#         }
#         return render(request, 'search.html', context)

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'index.html',{"message":message})
def add_usability(request, post_id):
    post = get_object_or_404(PostedSite, pk=post_id)
    # form = ReviewForm(request.POST)
    if request.method == 'POST':
        form = UsabilityForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.post = post
            rate.user_name = request.user
            rate.save()
        return redirect('home')

    return render(request, 'awards/post_list.html')

def add_design(request, post_id):
    post = get_object_or_404(PostedSite, pk=post_id)
    form = DesignForm()
    print('sasdffdddd')
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.post = post
            rate.user_name = request.user
            rate.save()
        return redirect('home')
    else:
        form = DesignForm()

    return render(request, 'awards/post_list.html',{'form': form})
def add_content(request, wine_id):
    post = get_object_or_404(PostedSite, pk=wine_id)
    # form = ReviewForm(request.POST)
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.post = post
            rate.user_name = request.user
            rate.save()
        return redirect('home')

    return render(request, 'awards/post_list.html')    
def vote(request, post_id):
    post = get_object_or_404(PostedSite, pk=post_id)
    # form = ReviewForm(request.POST)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.post = post
            vote.user = request.user
            vote.profile = request.user.profile

            vote.save()
        return redirect('home')

    return render(request, 'awards/post_list.html')

class CreateView(generics.ListCreateAPIView):
    '''
    this class defines the create behaviour of our rest api
    '''
    queryset = PostedSite.objects.all()
    serializer_class = PostedSiteSerializer

    def perform_create(self,serializer):
        '''
        Save the post data when creating a new postedsite.
        '''
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = PostedSite.objects.all()
    serializer_class = PostedSiteSerializer
