from rest_framework import serializers
from .models import OutBox


class OutBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutBox
        fields = ['id', 'mobile', 'message', 'status']
