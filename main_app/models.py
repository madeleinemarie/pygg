from django.db import models
from django.contrib.auth.models import User

CATEGORIES = (
    ('MC', 'Miscellaneous'),
    ('MO', 'Mortgage'),
    ('RE', 'Rent'),
    ('EN', 'Entertainment'),
    ('UT', 'Utilities'),
    ('IN', 'Insurance'),
    ('CC', 'Credit Cards'),
    ('LO', 'Loans')
)

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    budget = models.IntegerField()

class Bill(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(
        max_length=250,
        blank=True
    )
    amount = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    dueDate = models.DateField('Due Date')
    category = models.CharField(
        max_length=2,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    paid = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.name

    class Meta:
        ordering = ['-dueDate']
