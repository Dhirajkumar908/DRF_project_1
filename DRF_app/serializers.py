from rest_framework.serializers import ModelSerializer
from .models import *

class postSerializer(ModelSerializer):
    class Meta:
        model=post
        fields='__all__'
