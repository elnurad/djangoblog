from django.forms import ModelForm
from myblog.models import Post

class MyPostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'text', 'author']
