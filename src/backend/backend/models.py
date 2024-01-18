from django.db import models


class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=100, blank=True, default='')
    recipe = models.ForeignKey(
        Recipe, related_name='ingredients', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient


class Steps(models.Model):
    step = models.CharField(max_length=1000, blank=True, default='')
    recipe = models.ForeignKey(
        Recipe, related_name='steps', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.step
