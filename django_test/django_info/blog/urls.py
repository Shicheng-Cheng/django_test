
from django.urls import path,include
import blog.views

urlpatterns=[
    path('hello_world',blog.views.hello_world),
    path('content',blog.views.article_content),
    path('index',blog.views.get_index_page),
    #path('curr',blog.views.get_detail)
    path('curr/<int:article_id>',blog.views.get_detail)
]

#绑定了url的访问模式，均以blog开头，和views文件里的对应函数进行绑定。
#其中，get_detail函数接受两个参数，除了request，即id