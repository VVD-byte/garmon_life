from django.urls import path
from .views import Main, Paper_, Spec, Work_, Quest, PaperSlug, PaperNew

urlpatterns = [
    path('', Main.as_view(), name='MainPage'),
    path('paper/', Paper_.as_view(), name='PaperPage'),
    path('paper_new/', PaperNew.as_view(), name='PaperNew'),
    path('paper/<slug>/', PaperSlug.as_view(), name='PaperPageSlug'),
    path('spec/', Spec.as_view(), name='SpecPage'),
    path('work/', Work_.as_view(), name='WorkPage'),
    path('quest/', Quest.as_view(), name='QuestPage'),

]
