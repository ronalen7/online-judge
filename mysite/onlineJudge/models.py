from django.db import models

# Create your models here.


class Problem(models.Model):
    problem_name = models.CharField(max_length=200)
    problem_description = models.CharField(max_length=2000)
    constraints = models.CharField(max_length=100, default="")
    sample_input = models.CharField(max_length=300, default="")
    sample_output = models.CharField(max_length=300, default="")


def __str__(self):
    return self.problem_name
