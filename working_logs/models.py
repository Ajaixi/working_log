from django.db import models

# Create your models here.
class Project(models.Model):
    """施工项目申请单号"""
    text = models.CharField(max_length=200)
    date_added  = models.DateField()
    time_added = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Opinion(models.Model):
    """审批意见"""
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateField()
    time_added = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural  = 'Opinions'

    def __str__(self):
        return self.text[:50] + '...'