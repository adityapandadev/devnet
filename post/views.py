from django.db.models.query_utils import Q
from post.forms import PostForm
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.base import View
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your views here.

# View For Home Page
class HomeView(ListView):
    model = Post
    template_name = 'post/home.html'
    paginate_by = 6
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        post_list = Post.objects.filter(Q(caption__icontains = si)| Q(user__first_name__icontains = si)| Q(user__last_name__icontains = si)).order_by("-id")
        return Post.objects.filter(Q(caption__icontains = si)| Q(user__first_name__icontains = si)| Q(user__last_name__icontains = si)).order_by("-id")
        


# View for uploading content (add_post)
@method_decorator(login_required, name="dispatch")    
class PostCreateView(View):
    model = Post
    form_class = PostForm
    template_name = 'post/post.html'
    fields = '__all__'
    success_url = "home"
    
    
    
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name,{'form':form})
        
        
    def post(self,request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user;
            instance.save()
            return redirect(self.success_url)
        else:
            return render(request,self.template_name,{'form':form})