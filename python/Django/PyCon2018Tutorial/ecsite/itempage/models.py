from django.db import models


# Create your models here.
class Item(models.Model):
    item_code = models.CharField("商品コード", max_length=255, unique=True)
    item_name = models.CharField("商品名", max_length=255)
    price = models.PositiveIntegerField("価格")

    def __str__(self):
        return self.item_code

    class Meta:
        db_table = 'item'
        verbose_name = '商品'
        verbose_name_plural = "商品"


class OrderItem(models.Model):
    item_code = models.CharField("商品コード", max_length=255)
    item_name = models.CharField("商品名", max_length=255)
    price = models.PositiveIntegerField("価格")
    buy_num = models.PositiveIntegerField("数量")
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_code
    
    class Meta:
        db_table = 'order_item'
        verbose_name = "注文商品"
        verbose_name_plural = "注文商品"
    

class Order(models.Model):
    name = models.CharField("名前", max_length=255)
    address = models.CharField("住所", max_length=255)
    email = models.CharField("メールアドレス", max_length=255)
    order_time = models.DateTimeField("注文日時", auto_now_add=True)

    def __str__(self):
        return "{} 様の注文".format(self.name)
    
    class Meta:
        db_table = 'order'
        verbose_name = "注文"
        verbose_name_plural = "注文"

