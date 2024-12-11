from django.db import models
from datetime import date
import uuid

def get_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f"profile_images/{filename}"

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    password = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
        default="Select",
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.phone.startswith("+91-"):
            self.phone = f"+91-{self.phone}"
        super().save(*args, **kwargs)

# class Products(models.Model):
#     product_name = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     price = models.BooleanField
#     stock = models.IntegerField
#     image = models.ImageField(upload_to=get_image_upload_to)

# class Orders(models.Model):
#     order_date = models.DateField(default=date.today)
#     status = models
#     total_price = models
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', default=1)

# class Payment(models.Model):
#     Payment_date = models
#     amount = models
#     status = models
#     Payment_method = models
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='todos', default=1)
