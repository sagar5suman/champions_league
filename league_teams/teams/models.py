from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    is_super_qualifier = models.BooleanField(default=False)
    group = models.CharField(max_length=10, default='Unknown')
    stored_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' (' + self.state + ')'

    class Meta:
        db_table = 'club'