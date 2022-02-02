from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class ForgetPasswordModel(models.Model):
	verification_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	user_id = models.ForeignKey(User,on_delete = models.CASCADE,default = "")

	def __str__(self):
		return self.verification_id