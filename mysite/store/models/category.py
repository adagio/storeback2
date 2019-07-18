from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_name = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True, default='')

    def __str__(self):
        return self.product_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

