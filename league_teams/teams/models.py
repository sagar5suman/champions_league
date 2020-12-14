from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    is_super_qualifier = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' (' + self.state + ')'

    class Meta:
        db_table = 'club'