from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)  # เก็บข้อความยาวไม่เกิน 100 ตัวอักษร
    price = models.DecimalField(max_digits=10, decimal_places=2)  # เก็บตัวเลขทศนิยม
    created_at = models.DateTimeField(auto_now_add=True)  # เก็บเวลาที่สร้าง

    def __str__(self):
        return self.name
