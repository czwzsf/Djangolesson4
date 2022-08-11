from django import http
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from sight.models import Sight

from sight import serializers
from utils.response import NotFoundJsonResponse


class SightListView(ListView):
    """ 景点列表接口 """
    # 每页放5条数据
    paginate_by = 5

    def get_queryset(self):
        """ 重写查询方法 """
        query = Q(is_valid=True)
        # 1. 热门景点
        is_hot = self.request.GET.get('is_hot', None)
        if is_hot:
            query = query & Q(is_hot=True)
        # 2. 精选景点
        is_top = self.request.GET.get('is_top', None)
        if is_top:
            query = query & Q(is_top=True)
        queryset = Sight.objects.filter(query)
        return queryset

    # 为了能够将ListView生产的模版方法变成接口能够调用的数据，需要重写方法
    # 重点学习
    def render_to_response(self, context, **response_kwargs):
        page_obj = context['page_obj']
        if page_obj is not None:
            data = serializers.SightListSerializer(page_obj).to_dict()
            return http.JsonResponse(data)
        else:
            return NotFoundJsonResponse()
        # data = {
        #     'meta': {
        #         'total_count': page_obj.paginator.count,
        #         'page_count': page_obj.paginator.num_pages,
        #         'current_page': page_obj.number,
        #     },
        #     'objects': []
        # }
        # for item in page_obj.object_list:
        #     data['objects'].append({
        #         'id': item.id,
        #         'name': item.name,
        #         'img_url': item.main_img.url,
        #         'score': item.score,
        #         'province': item.province,
        #         'city': item.city,
        #         'min_price': item.min_price,
        #
        #         'comment_count': 0
        #     })
        # return http.JsonResponse(data)


class SightDetailView(DetailView):
    # TODO 面向对象的接口调用
    pass
