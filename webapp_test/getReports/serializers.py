from rest_framework.serializers import ModelSerializer
from .models import repoDetails

class RepoSerializer(ModelSerializer):
    class Meta:
        model = repoDetails
        fields = '__all__'