
from django.db import models

# Create your models here.
class info(models.Model) :
    booth_no=models.IntegerField()
    booth_name=models.CharField(max_length=40)
    par_consistuency=models.CharField(max_length=50)
    total_votes=models.IntegerField()


class voterinfo(models.Model) :
    vid=models.CharField(max_length=40)
    state=models.CharField(max_length=40)
    distno=models.IntegerField()
    distname=models.CharField(max_length=50)
    ac_no=models.IntegerField()
    ac_name=models.CharField(max_length=50)
    part_n0=models.IntegerField()
    part_name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    age=models.IntegerField()

class distrcred(models.Model):
    dist_name = models.CharField(max_length=100)
    distr_id = models.CharField(max_length=50)
    distr_pass = models.CharField(max_length=50)

class constcred(models.Model):
    const_name = models.CharField(max_length=100)
    district = models.ForeignKey(distrcred, on_delete=models.CASCADE)
    const_id = models.CharField(max_length=50)

class votercred(models.Model):
    voterid = models.CharField(max_length=50)
    voterpass = models.CharField(max_length=50)
    constituency = models.ForeignKey(constcred, on_delete=models.CASCADE)
