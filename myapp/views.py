from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.forms import modelformset_factory
from django.utils import timezone
from myapp.models import Post, MyPostForm

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('list.html')
    context = RequestContext(request, {'posts': posts})
    body = template.render(context)
    return HttpResponse(body, content_type="text/html")

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, 'detail.html', context)

def form_view(request):
 
    if request.method == "POST":
        form = MyPostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.author = "me"
            model_instance.save()
            return redirect('/')
 
    else:
 
        form = MyPostForm()
 
    return render(request, "form.html", {'form': form})