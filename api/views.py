from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer

def index(request):
    return render(request, 'index.html')

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    @action(detail=False, renderer_classes=[TemplateHTMLRenderer])
    def form(self, request):
        serializer = TweetSerializer()
        return Response({ 'serializer': serializer }, template_name = 'form_template.html')
