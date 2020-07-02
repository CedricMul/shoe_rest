from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=40)
    website = models.URLField(max_length=200)

class ShoeType(models.Model):
    style_choices = [
        ('SNKR', 'Sneaker'),
        ('BT', 'Boot'),
        ('SDL', 'Sandal'),
        ('DRS', 'Dress'),
        ('OTR', 'Other')
    ]
    style = models.CharField(
        max_length=4,
        choices=style_choices,
        default='SNKR'
        )

class ShoeColor(models.Model):
    color_choices = [
        ('BLK', 'Black'),
        ('WHT', 'White'),
        ('RED', 'Red'),
        ('ORNG', 'Orange'),
        ('YLLW', 'Yellow'),
        ('GRN', 'Green'),
        ('BLU', 'Blue'),
        ('INDG', 'Indigo'),
        ('VILT', 'Violet')
    ]
    color_name = models.CharField(
        max_length=4,
        choices=color_choices,
        default='BLK'
        )

class Shoe(models.Model):
    size = models.IntegerField(max_length=2)
    brand_name = models.CharField(max_length= 30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length= 20)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=15)
