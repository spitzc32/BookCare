from app.products.models import Product, ProductFeedback
from rest_framework import serializers, fields

class ProductSerializer(serializers.ModelSerializer):
    feedback = serializers.SerializerMethodField()

    class Meta:
    	model = Store
        fields = (
        	'id',
            'title', 
            'description', 
            'price', 
            'quantity_stock',
            'feedback',
        )

    def get_feedback(self, obj):	
        feedback_qs = ProductFeedback.objects.filter(
            account=obj.id,
            is_active=True,
        )

        serializer = ProductFeedbackSerializer(data=feedback_qs, many=True)
        serializer.is_valid()
        return serializer.data


class ProductFeedbackSerializer(serializers.ModelSerializer):
    
    class Meta:
    	model = Store
        fields = (
        	'id',
        	'feedback',
        )