from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    name= models.CharField(max_length=200)
    description = models.TextField(blank=True null=True)

   
class Priority(models.Model):
    level = models.CharField(max_length=50)
    level = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, null=True)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null=True, blank=True)
    Priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    def is_overdue(self)
        if self.due_date and timezone.now() > self.due_date and not self.completed:
            return True
        return False
    