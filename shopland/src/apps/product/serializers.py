from rest_framework import serializers
from .models import Product

# Были созданы сериализаторы в приложении product для удобной работы и изменений при дальнейшей поддержке и масштабировании проекта
class ProductSerializer(serializers.ModelSerializer): 
    # Сериалайзер для краткой информации о товаре, использует все поля модели 'Product'.
    class Meta:
        model = Product
        fields = "__all__"

class ProductDetailsSerializer(serializers.ModelSerializer):
    # Сериалайзер для детальной информации о товаре, также использует все поля модели 'Product'.
    class Meta:
        model = Product
        fields = "__all__"
