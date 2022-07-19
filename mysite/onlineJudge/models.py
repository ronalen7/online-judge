from django.db import models

# Create your models here.


class Problem(models.Model):
    problem_name = models.CharField(max_length=200)
    problem_description = models.CharField(max_length=2000)
    constraints = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.problem_name


class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=50)
    submitted_at = models.DateTimeField()
    submitted_code = models.CharField(max_length=255)

    def __str__(self):
        return self.verdict


class Testcase(models.Model):
    input = models.CharField(max_length=255)
    output = models.CharField(max_length=255)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return self.input
