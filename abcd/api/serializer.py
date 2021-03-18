from rest_framework import serializers
from django.apps import apps
Paper = apps.get_model('page', 'Paper')


class LikePaperSerialiser(serializers.ModelSerializer):
    like = serializers.SerializerMethodField()

    class Meta:
        model = Paper
        fields = ('like', )

    def get_like(self, obj):
        print(obj.like)
        return 1
