from django import http
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from sight.models import Sight, Comment, Ticket, Info

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
    def get_queryset(self):
        return Sight.objects.filter(is_valid=True)

    def render_to_response(self, context, **response_kwargs):
        page_obj = context['object']
        if page_obj is not None:
            data = serializers.SightDetailSerializer(page_obj).to_dict()
            return http.JsonResponse(data)


class SightCommentListView(ListView):
    """
    景点评论列表的接口
    """
    paginate_by = 10

    def get_queryset(self):
        # 根据景点ID查询景点
        # 获取网址上的id
        sight_id = self.kwargs.get('pk', None)
        sight = Sight.objects.filter(pk=sight_id, is_valid=True).first()
        if sight:
            # return Comment.objects.filter(is_valid=True, sight=sight)
            return sight.comments.filter(is_valid=True)
        return Comment.objects.none()

    def render_to_response(self, context, **response_kwargs):
        """ 重写响应的返回 """
        page_obj = context['page_obj']
        if page_obj is not None:
            data = serializers.CommentListSerializer(page_obj).to_dict()
            return http.JsonResponse(data)
        return NotFoundJsonResponse()


class SightTicketListView(ListView):
    """
    门票列表
    """
    paginate_by = 10

    def get_queryset(self):
        # 根据景点ID查询景点
        # 获取网址上的id
        sight_id = self.kwargs.get('pk', None)
        return Ticket.objects.filter(is_valid=True, sight__id=sight_id)

    def render_to_response(self, context, **response_kwargs):
        """ 重写响应的返回 """
        page_obj = context['page_obj']
        if page_obj is not None:
            data = serializers.TicketListSerializer(page_obj).to_dict()
            return http.JsonResponse(data)
        return NotFoundJsonResponse()


class SightInfoDetailView(DetailView):
    # 如果不使用slug_field将浏览器里面的pk指定为sight的主键，就会导致查询不出来我们所想要的景点信息，要与sight下的主键对应起来
    # TODO 结束后进行学习
    slug_field = 'sight__pk'

    def get_queryset(self):
        return Info.objects.all()

    def render_to_response(self, context, **response_kwargs):
        page_obj = context['object']
        if page_obj is not None:
            data = serializers.SightInfoSerializer(page_obj).to_dict()
            return http.JsonResponse(data)
        return NotFoundJsonResponse()
