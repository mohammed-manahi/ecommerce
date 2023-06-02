from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from django.db.models.functions import Lower


class Category(models.Model):
    """
    Create category model
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        """
        Define ordering and database indexing for category model
        """
        ordering = ['name', ]
        indexes = [models.Index(fields=['name']), models.Index(Lower('name').desc(), name='lower_category_name_idx')]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Define absolute url for category model based on slug field
        :return:
        """
        return f'/{self.slug}/'


class Product(models.Model):
    """
    Create product model
    """
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Define ordering and database indexing for product model
        """
        ordering = ['-created_at', 'name', ]
        indexes = [models.Index(fields=['name']), models.Index(Lower('name').desc(), name='lower_product_name_idx')]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Define absolute url for product model based on slug field of product and category
        :return:
        """
        return f'{self.category.slug}/{self.slug}/'

    def get_image(self):
        """
        Get image url using image url added to base url
        :return:
        """
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        """
        Get thumbnail url using thumbnail url added to base url
        :return:
        """
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.generate_thumbnail(self.image)
                self.save()
            else:
                ''

    def generate_thumbnail(self, image, size=(300, 200)):
        """
        Generate a thumbnail for product image with size 300*200
        :param image:
        :param size:
        :return:
        """
        # Convert image to RGB format and make thumbnail with given size
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        # save image extension and quality
        thumbnail_io = BytesIO()
        img.save(thumbnail_io, 'JPEG', quality=85)
        # Create thumbnail file with image name
        thumbnail = File(thumbnail_io, name=image.name)
        return thumbnail
