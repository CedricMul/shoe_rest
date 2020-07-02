from shoe_db_app.models import Manufacturer, ShoeColor, ShoeType, Shoe
from rest_framework import serializers

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            "name",
            "website"
        ]

class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            "color_name"
        ]

class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeType
        fields = [
            "style"
        ]

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            "size",
            "brand_name",
            "color",
            "material",
            "shoe_type",
            "fasten_type"
        ]
