from django.db import models
from django.urls import reverse
# Create your models here.


# CATEGORIES = (
# 	('Boys Summer', 'boys summer'),
# 	('Boys Winter', 'boys winter'),
# 	('girls Summer', 'girls summer'),
# 	('Girls Winter', 'girls summer'),
# 	('Kindergarten', 'kindergarten'),
# 	)







class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	sale_price = models.DecimalField(decimal_places=2, max_digits=100,\
												null=True, blank=True)
	slug = models.SlugField(unique=True)
	category    = models.ForeignKey('Category', on_delete=models.CASCADE, default = None)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	update_defaults = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price

	def get_absolute_url(self):
		return reverse("single", kwargs={"slug": self.slug})

	def get_all_products_by_categoryid(category_id):
		if category_id:
			return Product.objects.filter(category = category_id)
		else:
			return Product.objects.all()

	# def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Product,self).save(*args, **kwargs)
	#
    # def get_absolute_url(self):
    #     return self.slug


class Category(models.Model):
	parent = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE, default = None)
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ('slug', 'parent')
		verbose_name_plural = "categories"

	def get_absolute_url(self):
		return '/%s/' %(self.slug)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products/images', blank=True, null=True, default = None)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.title



class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)

	def sizes(self):
		return self.all().filter(category='size')

	# def colors(self):
	# 	return self.all().filter(category='color')



VAR_CATEGORIES = (
	('size', 'size'),
	# ('color', 'color'),
	('package', 'package'),
	)


class Variation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.PROTECT)
	category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
	title = models.CharField(max_length=120)
	image = models.ForeignKey(ProductImage, null=True, blank=True, on_delete=models.PROTECT)
	price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	objects = VariationManager()

	def __str__(self):
		return self.title
