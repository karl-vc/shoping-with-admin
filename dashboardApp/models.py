from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.text import slugify
import random
import string


def generate_slug_value(length=10):
	return "".join(random.choice(string.ascii_letters) for _ in range(length))


class ProductDetail(models.Model):

	product_name = models.CharField(max_length= 200, default="")
	product_price = models.PositiveIntegerField( default=1,
        validators=[
            MaxValueValidator(100000,('Way over %(limit_value)s.')),
           
        ])
	
	product_description = models.TextField(default ="")
	product_image = models.ImageField(upload_to='images/')
	time_left = models.PositiveIntegerField( default=1,
        validators=[
            MaxValueValidator(20,('Way over %(limit_value)s.')),
           
        ])
	total_buyers = models.PositiveIntegerField( default=1,
        validators=[
            MaxValueValidator(20,('Way over %(limit_value)s.')),
           
        ])
	slug = models.SlugField(unique=True,blank=True,null=True)
	is_delete = models.BooleanField(default = False)

	# slug starts from here
	def save(self, *args, **kwargs):
		self.slug = slugify(generate_slug_value())
		super(ProductDetail, self).save(*args, **kwargs)


	def __str__(self):
		return self.product_name

	# def another_images_count(self):
	# 	return ProductImages.objects.filter(product_id=self).count()



class ProductImages(models.Model):

	product_pictures = models.ImageField(upload_to ='images/')
	product_id = models.ForeignKey(ProductDetail,on_delete = models.CASCADE,default = "")

	def __str__(self):
		return self.product_pictures.name
