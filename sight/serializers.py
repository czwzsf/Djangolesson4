"""
重构化使用
"""
from utils.serializers import BaseListPageSerializer


class SightListSerializer(BaseListPageSerializer):
    """ 景点列表 """

    def get_object(self, obj):
        return {
            'id': obj.id,
            'name': obj.name,
            'main_img': obj.main_img.url,
            'score': obj.score,
            'province': obj.province,
            'min_price': obj.min_price,
            'city': obj.city,
            # TODO 评论数量暂时无法获取
            'comment_count': 0
        }
