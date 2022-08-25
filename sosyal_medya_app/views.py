from requests import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Post
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required(login_url='/login')
def anasayfa(request):
    postlar = Post.objects.all()
    content = {
        'postlar' : postlar 
    }

    #sil
    if request.method == 'POST':
        post_id = request.POST.get('id')
        degisecek_post = postlar.filter(id = post_id).first()
        if degisecek_post:
            if degisecek_post.yazar == request.user or request.user.has_perm('sosyal_medya_app.delete_post'):
                degisecek_post.delete()
        

    return HttpResponse( render( request, 'main/anasayfa.html', content ) )

def kayit(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('anasayfa')
    else:
        form = RegisterForm()
    return HttpResponse( render( request, 'registration/kayit.html', {'form': form} ) )

@login_required(login_url='/login')
@permission_required('sosyal_medya_app.add_post', raise_exception=True, )
def paylas(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.yazar = request.user
            post.save()
            return redirect('anasayfa')
    else:
        form = PostForm()

    return HttpResponse( render( request, 'main/paylas.html', {'form': form} ) )
