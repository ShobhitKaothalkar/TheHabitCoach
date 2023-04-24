from django.db import models
from users.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ongoing = models.BooleanField(default=True)
    daily_or_weekly = models.CharField(max_length=10, choices=(('D', 'Daily'), ('W', 'Weekly')))
    duration = models.IntegerField()


    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('habit-detail', kwargs={'pk': self.pk})

class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.IntegerField()

    def __str__(self):
        return f"{self.habit}, {self.date}, {self.value}"
    
    def get_absolute_url(self):
        return reverse('habit-detail', kwargs={'pk': self.habit_id})

