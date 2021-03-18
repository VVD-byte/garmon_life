from rest_framework.generics import ListCreateAPIView
from .serializer import LikePaperSerialiser
from django.apps import apps
Paper = apps.get_model('page', 'Paper')


class Like(ListCreateAPIView):
    model = Paper
    serializer_class = LikePaperSerialiser

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        return Paper.objects.filter(slug=slug)
