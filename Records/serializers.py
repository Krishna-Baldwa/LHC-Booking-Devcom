from rest_framework import serializers
from . models import halls

class hallsSerializer(serializers.ModelSerializer):

    class Meta:
        model= halls
        fields='__all__'
