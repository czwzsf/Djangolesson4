"""
重构化使用
"""
from utils.serializers import BaseListPageSerializer, BaseSerializer


class SightListSerializer(BaseListPageSerializer):
    """ 景点列表 """

    def get_object(self, obj):
        return {
            'id': obj.id,
            'name': obj.name,
            'img_url': obj.main_img.url,
            'score': obj.score,
            'province': obj.province,
            'min_price': obj.min_price,
            'city': obj.city,
            # TODO 评论数量暂时无法获取
            'comment_count': 0
        }


class SightDetailSerializer(BaseSerializer):
    """ 景点详情 """

    def to_dict(self):
        obj = self.obj
        return {
            'id': obj.id,
            'name': obj.name,
            'desc': obj.desc,
            'img': obj.banner_img.url,
            'content': obj.content,
            'score': obj.score,
            'min_price': obj.min_price,
            'province': obj.province,
            'city': obj.city,
            'area': obj.area,
            'town': obj.town,
            # TODO 评论数量暂时无法获取
            'comment_count': 0
        }
