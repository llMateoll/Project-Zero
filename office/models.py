from django.db import models

# Create your models here.

class Level(models.Model):
    level = models.TextField(max_length=20, null=False, blank=False)
    price = models.DecimalField(max_digits=30, decimal_places=2, default='0.00')
    reference = models.TextField(max_length=20, null=False, blank=False)

    class Meta:
        ordering = ['level']

    # def __str__(self):
    #     return self.user

    # pk = models.Field(primary_key = True)


# 1 - 1
# 2 - 5
# 3 - 20
# 4 - 100
# 5 - 200
# 6 - 1000
# 7 - 2000