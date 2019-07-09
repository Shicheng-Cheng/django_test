from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import  Paginator
from blog.models import Article
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world")

def article_content(request):
    article=Article.objects.all()[0]
    title=article.title
    content=article.content
    article_id=article.article_id
    brief_content=article.brief_content
    publish_data=article.publish_data
    return_str='title:%s,brief_content: %s'%(title,content)
    return HttpResponse(return_str)

def get_index_page(request):
    page=request.GET.get('page')
    if page:
        page=int(page)
    else:
        page=1
    print("page:",page)
    all_article=Article.objects.all()
    top_article=Article.objects.order_by("-publish_data")[:]
    paginator=Paginator(all_article,1)
    page_num=paginator.num_pages
    print('num:',paginator.num_pages)
    page_list=paginator.page(page)
    if page_list.has_next():
        next_page=page+1
    else:
        next_page=page
    if page_list.has_previous():
        previous_page=page-1
    else:
        previous_page=page
    return render(request,"blog/index.html",
                  {
        'article_list':page_list,
        'page_num':range(1,page_num+1),
        'curr_page':page,
        'next_page':next_page,
        'previous_page':previous_page,
        'top_article':top_article
    })

def get_detail(request,article_id):
    all_article=Article.objects.all()
    curr_article=None
    pre_index=0
    next_index=0
    for index,article in enumerate(all_article):
        if index==0:
            pre_index=0
            next_index=index+1
        elif index==len(all_article)-1:
            pre_index=index-1
            next_index=index
        else:
            pre_index=index-1
            next_index=index+1
        if article.article_id==article_id:
            curr_article=article
            pre_article=all_article[pre_index]
            next_article=all_article[next_index]
            break
    section=curr_article.content.split('\n')
    return render(request,'blog/detail.html',
                  {
                      'curr_article':curr_article,
                      'section':section,
                      'previous':pre_article,
                      'next':next_article
                  }
                  )
