#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def blog(request):
#    if request.method == "GET":
        # for us to get the specific article for the user
#        pass
#    elif request.method == "POST":
        # Create a new article with this id
#        pass
#    elif request.method == "PUT":
        # update the entire article
#        pass
#    elif request.method == "DELETE":
        # delete this article
#        pass
#    return HttpResponse(f"<h1>Blog</h1>")
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from .models import Article
#from .forms import ArticleForm
#import json

#def blog(request):
#    if request.method == "GET":
#        # Retrieve specific article based on ID, or list all articles if no ID is provided
#        article_id = request.GET.get('id')
#        if article_id:
#            article = get_object_or_404(Article, id=article_id)
#            data = {
#                    'title': article.title,
#                    'content': article.content,
#                    'author': article.author.username,
#                    'published_date': article.published_date,
#                    }
#            return JsonResponse(data)
#        else:
#            articles = Article.objects.all()
#            data = [{'id': article.id, 'title': article.title} for article in articles]
#            return JsonResponse(data, safe=False)
#    elif request.method == "POST":
#        # Create a new article
#        data = json.loads(request.body)
#        form = ArticleForm(data)
#        if form.is_valid():
#            article = form.save(commit=False)
#            article.author = request.user  # Assuming the user is authenticate
#            article.save()
#            return JsonResponse({'message': 'Article created successfully', 'id': article.id}, status=201)
#        else:
#            return JsonResponse(form.errors, status=400)
#    elif request.method == "PUT":
#        # Update the entire article
#        data = json.loads(request.body)
#        article_id = data.get('id')
#        if not article_id:
#            return JsonResponse({'error': 'Article ID is required'}, status=400)
#        article = get_object_or_404(Article, id=article_id)
#        form = ArticleForm(data, instance=article)
#        if form.is_valid():
#            form.save()
#            return JsonResponse({'message': 'Article updated successfully'})
#        else:
#            return JsonResponse(form.errors, status=400)
#    elif request.method == "DELETE":
#        # Delete the article data = json.loads(request.body)
#        article_id = data.get('id')
#        if not article_id:
#            return JsonResponse({'error': 'Article ID is required'}, status=400)
#        article = get_object_or_404(Article, id=article_id)
#        article.delete()
#       return JsonResponse({'message': 'Article deleted successfully'})
#    return HttpResponse("<h1>Blog</h1>")

#from .models import Post
def blog_post(request, article_id):
    return render(request, 'blog/post.html')
def blog_archive(request):
    return render(request, 'blog/index.html')

#def blog_index(request):
#    posts = Post.objects.all().order_by('-published_date')
#    return render(request, 'index.html', {'posts': posts})

#def post_detail(request, post_id):
#    post = get_object_or_404(Post, id=post_id)
#    return render(request, 'post.html', {'post': post})
