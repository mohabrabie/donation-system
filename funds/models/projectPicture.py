from django.db import models
from .project import Project


class ProjectPicture(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    project = models.ForeignKey(Project, on_delete=models.NOT_PROVIDED)

    def __str__(self):
        return f"{self.project.__str__()} img"
