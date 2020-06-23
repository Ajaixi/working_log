from django.db import models

# Create your models here.
class Project(models.Model):
    """施工项目申请单号"""
    text = models.CharField(max_length=200)
    date_added  = models.DateField()
    time_added = models.TimeField(auto_now_add=True)
    STATE_CHOICES = (
        ('pending', 'pending'),
        ('reviewed', 'reviewed'),
    )
    state = models.CharField(max_length=15, choices=STATE_CHOICES, default='pending')

    def __str__(self):
        return self.text
    
    class Meta:
        permissions = (("can_approve_or_reject_project", "Can approve or reject project"),)


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


class Img(models.Model):
    """添加图片"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    img_url = models.FileField(upload_to='photos/',blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    #name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Imgs'
    
    def __str__(self):
        return str(self.date_added)


