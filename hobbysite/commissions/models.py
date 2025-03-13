from django.db import models

# Create your models here.

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created_on']

class Comment(models.Model):
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE
    )
    entry = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

