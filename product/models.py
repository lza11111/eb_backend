from django.db import models

# Create your models here.
class Company(models.Model):
    sup_no = models.AutoField(primary_key=True)
    sup_name = models.CharField(max_length=30)

    def __str__(self):
        return self.sup_name

    class Meta:
        managed = False
        db_table = 'Company'


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=8)
    cust_code = models.CharField(max_length=12)
    addr = models.CharField(max_length=40)
    regis_date = models.DateTimeField(blank=True, null=True)
    zip = models.CharField(max_length=6)
    tel_no = models.CharField(max_length=11)
    sex = models.CharField(max_length=2)
    cust_level = models.ForeignKey('Discount', models.DO_NOTHING, db_column='cust_level')
    cust_sco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cust_name

    class Meta:
        managed = False
        db_table = 'Customer'


class Delivery(models.Model):
    deliv_no = models.AutoField(primary_key=True)
    deliv_date = models.DateTimeField()
    order_no = models.ForeignKey('Sale', models.DO_NOTHING, db_column='order_no')
    prod = models.ForeignKey('Product', models.DO_NOTHING)
    prod_name = models.CharField(max_length=20)
    qty = models.IntegerField()
    cust = models.ForeignKey(Customer, models.DO_NOTHING)
    cust_name = models.CharField(max_length=8)
    addr = models.CharField(max_length=40)
    zip = models.CharField(max_length=6)
    tel_no = models.CharField(max_length=11)
    deliv_status = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'Delivery'


class Discount(models.Model):
    cust_level = models.AutoField(primary_key=True)
    discount = models.DecimalField(max_digits=7, decimal_places=2)
    sco_re = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'Discount'


class Kind(models.Model):
    kind_no = models.AutoField(primary_key=True)
    kind_name = models.CharField(max_length=15)

    def __str__(self):
        return self.kind_name

    class Meta:
        managed = False
        db_table = 'Kind'


class Product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=20)
    prod_date = models.DateTimeField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    storaging = models.IntegerField()
    sup_no = models.ForeignKey(Company, models.DO_NOTHING, db_column='sup_no')
    kind_no = models.ForeignKey(Kind, models.DO_NOTHING, db_column='kind_no')
    supply = models.IntegerField()
    wh_no = models.ForeignKey('Warehouse', models.DO_NOTHING, db_column='wh_no')

    def __str__(self):
        return self.prod_name

    class Meta:
        managed = False
        db_table = 'Product'


class Return(models.Model):
    chan_no = models.AutoField(primary_key=True)
    cust = models.ForeignKey(Customer, models.DO_NOTHING)
    order_no = models.ForeignKey('Sale', models.DO_NOTHING, db_column='order_no')
    chan_date = models.DateTimeField(blank=True, null=True)
    chan_status = models.CharField(max_length=2, blank=True, null=True)
    prod = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Return'
        unique_together = (('chan_no', 'cust', 'order_no'),)


class Sale(models.Model):
    order_no = models.AutoField(primary_key=True)
    cust = models.ForeignKey(Customer, models.DO_NOTHING)
    tot_amt = models.DecimalField(max_digits=7, decimal_places=2)
    order_date = models.DateTimeField()
    invoice_no = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'Sale'


class SaleItem(models.Model):
    order_no = models.ForeignKey(Sale, models.DO_NOTHING, db_column='order_no', primary_key=True)
    prod = models.ForeignKey(Product, models.DO_NOTHING)
    tot_amt = models.DecimalField(max_digits=7, decimal_places=2)
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=2)
    dis_price = models.DecimalField(max_digits=7, decimal_places=2)
    qty = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    cust_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Sale_item'
        unique_together = (('order_no', 'prod'),)


class Shopcart(models.Model):
    shop_no = models.AutoField(primary_key=True)
    cust = models.ForeignKey(Customer, models.DO_NOTHING)
    prod = models.ForeignKey(Product, models.DO_NOTHING)
    prod_name = models.CharField(max_length=20)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    dis_price = models.DecimalField(max_digits=7, decimal_places=2)
    qty = models.IntegerField()
    buy = models.CharField(max_length=4)
    pro_totamt = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'Shopcart'
        unique_together = (('shop_no', 'prod'),)


class Warehouse(models.Model):
    wh_no = models.AutoField(primary_key=True)
    wh_name = models.CharField(max_length=10)

    def __str__(self):
        return self.wh_name

    class Meta:
        managed = False
        db_table = 'Warehouse'