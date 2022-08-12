from utils.serializers import BaseSerializer


class BaseImageSerializer(BaseSerializer):
    """ 序列化基础图片：其它列表需要引用到时使用 """

    def to_dict(self):
        image = self.obj
        return {
            'img': image.img.url,
            'summary': image.summary
        }


class SliderListSerializer(BaseSerializer):
    def to_dict(self):
        item = self.obj
        return {
            'id': item.id,
            'img_url': item.img.url,
            'target_url': item.target_url,
            'name': item.name
        }
