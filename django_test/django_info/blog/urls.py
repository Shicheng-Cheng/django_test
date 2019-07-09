
from django.urls import path,include
import blog.views

urlpatterns=[
    path('hello_world',blog.views.hello_world),
    path('content',blog.views.article_content),
    path('index',blog.views.get_index_page),
    #path('curr',blog.views.get_detail)
    path('curr/<int:article_id>',blog.views.get_detail)
]