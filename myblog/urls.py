from django.urls import path
from .views import stub_view
from .views import list_view
from .views import detail_view

urlpatterns = [
    path('',
    	list_view,
    	name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]