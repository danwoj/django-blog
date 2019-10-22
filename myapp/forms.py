from django.forms import ModelForm
from myapp.models import Post
 
class MyPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'created_date']