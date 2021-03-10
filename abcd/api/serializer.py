from rest_framework import serializers
from page.models import Paper


class LikePaperSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Paper
        fields = '__all__'
