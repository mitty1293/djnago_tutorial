from django.contrib import admin

from .models import Department, Employee, Position, Skill, SkillCategory

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Skill)
admin.site.register(SkillCategory)
