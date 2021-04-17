from django.contrib import admin

from .models import Product, ProductImage, Variation, Category, School
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp' #updated
	search_fields = ['title', 'description']
	list_display = ['title', 'price', 'active', 'updated']
	list_editable = ['price', 'active']
	list_filter = ['price', 'active']
	readonly_fields = ['updated', 'timestamp']
	prepopulated_fields = {"slug": ("title",)}
	class Meta:
		model = Product


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']


class SchoolAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name", )}
	list_display = ['name', 'slug', 'address', 'phone']
	class Meta:
		model = School

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Variation)
admin.site.register(School, SchoolAdmin)
# admin.site.register(Category)
admin.site.register(Category, CategoryAdmin)
