from django.db import models


class Vendor(models.Model):
    vendor_type_choices=(
        ('Domestic', 'Domestic'),
        ('International', 'International')
        )
    name                    = models.CharField(verbose_name="Name", max_length=100, null=True, blank=True)
    contact                 = models.TextField(verbose_name="contact", null=True, blank=True)
    address                 = models.TextField(verbose_name="address", max_length=200, null=True, blank=True)
    vendor_code             = models.CharField(verbose_name="code", max_length=50, null=True, blank=True, unique=True)
    on_time_delivery_rate   = models.FloatField(default=0.0)
    quality_rating_avg      = models.FloatField(default=0.0)
    average_response_time   = models.FloatField(default=0.0)
    fulfillment_rate        = models.FloatField(default=0.0)   
    type                    = models.CharField(verbose_name = "type", choices=vendor_type_choices, max_length = 255, null=False, blank=False)
    name                    = models.CharField(verbose_name='name',max_length=100, null=False, blank=False, unique=True)
    address                 = models.CharField(verbose_name='address',max_length=10000, null=False, blank=False)
    pincode                 = models.PositiveIntegerField(verbose_name='pincode', null=True, blank=True)
    state                   = models.CharField(verbose_name='state',max_length=100, null=True, blank=True)
    city                    = models.CharField(verbose_name='city', max_length=100, null=True, blank=True)
    country                 = models.CharField(verbose_name='country', max_length=100, null=False, blank=False, default='India')
    website                 = models.URLField(verbose_name='website', max_length=200, null=True, blank=True)
    estd_date               = models.DateField(verbose_name='Date of Establishment', null=True, blank=True)
    gst_number              = models.CharField(verbose_name='gst number', max_length=100, null=True, blank=True)
    pan_number              = models.CharField(verbose_name='pan number', max_length=100, null=True, blank=True)

    total_sales_turnover    = models.PositiveBigIntegerField(verbose_name='total sales turnover', null=True, blank=True)

    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.type               = self.type
        self.name               = self.name
        self.address            = self.address
        self.pincode            = self.pincode
        self.state              = self.state
        self.city               = self.city
        self.country            = self.country

        self.website            = self.website
        self.estd_date          = self.estd_date
        self.gst_number         = self.gst_number
        self.pan_number         = self.pan_number
        
        super(Vendor, self).save()
    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    vendor_type_choices=(
        ('International','International'),
        ('Domestic', 'Domestic'),
    )
    vendor_type         = models.CharField(verbose_name = "vendor type", choices=vendor_type_choices, max_length = 255, default= 'Domestic')
    po_date             = models.DateField(verbose_name='Purchase Order date', null=True, blank=True)
    po_number           = models.CharField(verbose_name='purchase order number', max_length=100, null=False, blank=False, unique=True)
    schedule_date       = models.DateField(verbose_name='schedule date', null=True, blank=True)
    payment_terms       = models.CharField(verbose_name='payment terms', max_length=200, null=True, blank=True)
    delivery_terms      = models.CharField(verbose_name='delivery terms', max_length=200, null=True, blank=True)
    status              = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', null=True, blank=True)
    vendor              = models.ForeignKey(Vendor,on_delete=models.SET_NULL, null=True, blank=True)
    vendor_contact      = models.TextField(verbose_name='contact', null=True, blank=True)
    vendor_email        = models.EmailField(verbose_name='email', null=True, blank=True)
    vendor_contact_person = models.CharField(verbose_name='contact person', max_length=100, null=True, blank=True)
    amount              = models.DecimalField(verbose_name='amount', null=True, blank=True , max_digits=50, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.po_date = self.po_date
        self.schedule_date = self.schedule_date
        super(PurchaseOrder, self).save()

    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date_recorded = models.DateField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return f"Performance on {self.date_recorded} for {self.vendor.name}"

