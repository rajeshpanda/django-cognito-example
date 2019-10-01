from rest_framework import serializers
from . models import talent

class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = talent
        fields = '__all__'