from django.db import models


class MyNewsletter(models.Model):
    title = models.CharField(max_length=100)
    header_content = models.CharField(max_length=500, )
    body_content = models.TextField(null=True,blank=True)
    footer_content = models.CharField(max_length=500,)
    created_on = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.title


