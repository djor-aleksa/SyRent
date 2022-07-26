from django.contrib import admin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class GeneralSetting(models.Model):
    company_name = models.CharField(max_length=30)
    company_phone = models.CharField(max_length=15)
    company_address = models.CharField(max_length=100)
    company_email_address = models.EmailField(max_length=100)
    bank_account_number = models.CharField(max_length=34)
    default_currency = models.CharField(max_length=3, default="RSD")
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    timezone = models.CharField(max_length=32, choices=TIMEZONES)
    active = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.active:
            # select all other active items
            qs = type(self).objects.filter(active=True)
            # except self (if self already exists)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            # and deactivate them
            qs.update(active=False)

        super(GeneralSetting, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.company_name}, {self.company_address}'


class ItemCategory(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Item categories"

    def __str__(self):
        return self.name


class RentalItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    notes = models.TextField(max_length=600)  # can contain details on current state of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='RSD')
    minimal_rental_period_days = models.IntegerField(default=0)
    category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True)

    def rental_price_per_day(self):
        return f'{self.price} {self.currency}'

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Customer(models.Model):

    email_address = models.EmailField(max_length=100, verbose_name='e-mail address')
    company = models.CharField(max_length=30, verbose_name='Company name')
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: "
                "'+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(
        max_length=16,
        validators=[phone_regex], verbose_name='Phone number')
    address = models.CharField(max_length=60)
    note = models.TextField(max_length=600, blank=True)

    def __str__(self):
        return f'{self.company} - {self.name} {self.surname}'

    class CustomerType(models.TextChoices):
        PRIVATE_PERSON = 'PP', _('Private person')
        COMPANY = 'CP', _('Company')

    customer_type = models.CharField(
            max_length=2,
            choices=CustomerType.choices
        )


class RentalContract(models.Model):
    start_datetime = models.DateTimeField(null=True, verbose_name='Rental start')
    end_datetime = models.DateTimeField(null=True, verbose_name='Rental end')
    actual_end_date = models.DateTimeField(null=True, blank=True, verbose_name=' Rental items reclamation date')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    overdue_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='RSD')
    price_without_discount = models.DecimalField(max_digits=10, decimal_places=2)
    rental_items = models.ManyToManyField(RentalItem)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.customer.name}-{self.pk}'

    class PaymentStatus(models.TextChoices):
        NOT_PAID = 'NP', _('Not paid')
        PAID = 'OK', _('Paid')
        EXEMPT = 'EX', _('Exempt')
        REFUNDED = 'RF', _('Refunded')
        FAILED = 'FL', _('Failed')
        CANCELLED = 'CX', _('Cancelled')
        OVERDUE = 'OD', _('Overdue')

    payment_status = models.CharField(
        max_length=2,
        choices=PaymentStatus.choices
    )











