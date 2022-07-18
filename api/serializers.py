from trading.models import Product,Comment,Profile
from rest_framework.serializers import ModelSerializer

class ProductSerializer(ModelSerializer):
    class Meta :
        model = Product
        fields = ['name','price','type_of','brand','image']