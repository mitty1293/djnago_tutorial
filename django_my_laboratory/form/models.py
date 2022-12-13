from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    age = models.PositiveSmallIntegerField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
