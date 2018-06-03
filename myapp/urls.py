from django.conf.urls import url
from myapp.views import list_view, detail_view, form_view
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
    url(r'^$', list_view, name="blog_index"),
    url(r'^posts/new/$', form_view, name="submit_post")
#    url(r'^.*$', RedirectView.as_view(pattern_name="blog_index", permanent=False), name="index")
]