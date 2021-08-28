from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=30,
        style={'placeholder': 'Name'}
    )
    text = serializers.CharField(
        max_length=50,
        style={'base_template': 'textarea.html', 'placeholder': 'Write Tweet...'}
    )
    class Meta:
        model = Tweet
        fields = '__all__'