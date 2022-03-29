import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Post
from .api.serializers import PostSerializer


@csrf_exempt
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return JsonResponse({'data': PostSerializer(posts, many=True).data})
    elif request.method == "POST":
        post_data = json.loads(request.body)
        serializer = PostSerializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return JsonResponse(PostSerializer(post).data)

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    import logging
    logger = logging.getLogger(__name__)
    logger.info(request.method)

    if request.method == "GET":
        return JsonResponse(PostSerializer(post).data)
    elif request.method == "PUT":
        post_data = json.loads(request.body)
        serializer = PostSerializer(post, data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)
    elif request.method == "DELETE":
        logger.info('Deleting post {}', post)
        post.delete()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])
