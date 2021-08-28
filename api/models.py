from django.db import models

# Create your models here.
class Tweet(models.Model):
    text = models.CharField(max_length=50, help_text="Write Tweet...")
    username = models.CharField(max_length=30, help_text="Name")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"
    
    def __str__(self):
        return f'{self.id} - {self.username}'