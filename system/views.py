from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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
