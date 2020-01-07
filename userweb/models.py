from django.db import models
from django.contrib.auth.models import User
from penjadwalan.models import *
# Create your models here.

# class StudentAccount(models.Model):
#     user        = models.OneToOneField(User, on_delete=models.CASCADE)
#     nik         = models.CharField(max_length=25)
#     first_name  = models.CharField(max_length=25)
#     last_name   = models.CharField(max_length=25)
#     kelas       = models.ForeignKey(Kelas, on_delete=models.CASCADE)

#     def __str__(self):
#         return '{} {}'.format(self.nik, self.first_name)

# class TeacherAccount(models.Model):
#     user        = models.OneToOneField(User, on_delete=models.CASCADE)
#     guru        = models.ForeignKey(Guru, max_length=25, on_delete=models.CASCADE)

#     def __str__(self):
#         return '{}'.format(self.guru)


