from django.views.generic.base import TemplateView
from accounts.models import CustomUser, Friend_Request, Profile
from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from accounts.forms import UserForm
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.db.models.query_utils import Q
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model


from django.conf import settings
User = settings.AUTH_USER_MODEL


def register(req):
    form = UserForm()
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(req, 'register.html', {'form': form})


#View for Profile template where all posts uploaded by requested user will be shown
@login_required
def profile(request):
    log_user = request.user            
    post = Post.objects.filter(user = log_user).order_by("-id")
    return render(request,'profile.html',{'m':post})


# View for Explore dev template where list of all the registered user will be shown
class ExploreView(ListView):
    template_name = 'explore.html'
    model = CustomUser

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = ""
        object_list = CustomUser.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
        return object_list



# to Send Friend Request 
@login_required
def send_request(request, userID):
    from_user = request.user
    to_user = get_user_model().objects.get(id=userID)
    friend_request, created = Friend_Request.objects.get_or_create(
        from_user = from_user, to_user=to_user
    )
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request was already sent')

#  To Accept friend request
@login_required
def accept_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request not accepted')

