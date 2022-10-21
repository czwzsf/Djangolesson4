from django.core.cache import cache
from django.http import JsonResponse, HttpResponse

# Create your views here.
from system.models import Slider


def slider_list(request):
    """
    轮播图的接口
    :param request:
    :type request:
    :return:
    {
        "meta": {},
        "objects": []
    }
    :rtype:
    """
    data = {
        'meta': {},
        'objects': []
    }
    queryset = Slider.objects.filter(is_valid=True)
    for item in queryset:
        data['objects'].append({
            'id': item.id,
            'img_url': item.img.url,
            'target_url': item.target_url,
            'name': item.name
        })
    return JsonResponse(data)


def cache_set(request):
    """写缓存"""
    # cache.set('username', 'lisi')
    cache.set('password', 'password', timeout=20)
    return HttpResponse("ok")


def cache_get(request):
    """读缓存"""
    value = cache.get('password')
    return HttpResponse(value)
