from django.shortcuts import render, get_object_or_404
from .forms import UploadForm
from .models import UploadImage 
from django.http import Http404, JsonResponse

# Create your views here.

def index(request):
    articles = UploadImage.objects.order_by("-id")
    context = {
        "articles" : articles
    }
    return render(request, 'teamapp/index.html', context)

def upload(request):
    params = {
        'upload_form': UploadForm(),
        'id': None,
        'title': None,
        'detail': None,
        'point': None,
        'dissapoint': None,
        
    }
    

    if (request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()
            params['id'] = upload_image.id
            params['title'] = upload_image.title
            params['detail'] = upload_image.detail
            params['point'] = upload_image.point
            params['dissapoint'] = upload_image.dissapoint    

    return render(request, "teamapp/upload.html", params)


def preview(request, image_id=0):

    upload_image = get_object_or_404(UploadImage, id=image_id)

    params = {
        'id' : upload_image.id, 
        'title': upload_image.title,
        'url': upload_image.image.url,
        'detail':upload_image.detail,
        'point': upload_image.point,
        'dissapoint': upload_image.dissapoint,
        'like' : upload_image.like
    }

    return render(request, 'teamapp/preview.html', params)

def api_like(request, article_id):
    try:
        article = UploadImage.objects.get(pk=article_id)
        article.like += 1
        article.save()
    except UploadImage.DoesNotExist:
        raise Http404("Article does not exist")
        
    result = {
        'id' : article_id,
        'like' : article.like
    }
    return JsonResponse(result)
