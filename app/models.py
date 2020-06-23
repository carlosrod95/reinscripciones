

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	nombre = models.CharField(max_length=50, blank=True)
	apepaterno = models.CharField(max_length=100, blank=True)
	apematerno = models.CharField(max_length=100, blank=True)
	curp = models.CharField(max_length=18, blank=True)
	matricula = models.CharField(max_length=10, blank=True)
	GRADO_TYPE_CHOICES = (
      (1, '1'),
	  (2, '2'),
	  (3, '3'),
	  (4, '4'),
	  (5, '5'),
	  (6, '6'),
    )
	
	ESCUELA_TYPE_CHOICES = (
      (1, 'SINDICATO ALBA ROJA NUM. 20 02EES0212Q'),
    )
	escuela_type = models.PositiveSmallIntegerField(choices=ESCUELA_TYPE_CHOICES)
	tutor = models.CharField(max_length=40,verbose_name="Nombre Tutor:  ",null=None,blank=False)
	grado = models.IntegerField(default=1,choices=GRADO_TYPE_CHOICES)
	grupo = models.CharField(max_length=1,default='A')
	fechanacimiento = models.DateTimeField(max_length=8)
	def __str__(self):
		return "%s %s %s %s %s" % ( self.apepaterno, self.apematerno, self.nombre, self.curp ,self.user)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()