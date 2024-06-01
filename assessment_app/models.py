from django.db import models

# Create your models here.


class Userdetails(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    created_dt = models.DateTimeField(blank=True, null=True)



class FrndRequest(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    fk_user = models.ForeignKey(Userdetails, on_delete=models.CASCADE , related_name="my_user_id", blank=True, null=True )
    fk_request_user = models.ForeignKey(Userdetails, on_delete=models.CASCADE , related_name="request_sended_user_id", blank=True, null=True )
    request_status = models.CharField(max_length=200, choices=STATUS, blank=True, null=True, default='Pending')
    created_dt = models.DateTimeField(blank=True, null=True)