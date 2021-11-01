from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.core.validators import MaxValueValidator, MinValueValidator, slug_re
from django.urls import reverse
from django.db.models.signals import pre_save


from .utils import unique_slug_generator
# Create your models here.

class Caterer(models.Model):
    business_name  = models.CharField(max_length=120)
    slug           = models.SlugField(blank=True)
    address        = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.business_name
    
    def get_absolute_url(self):
        #return reverse("caterer detail", args=[str(self.slug)])
        return "/caterers/{slug}/".format(slug=self.slug)


class Service(models.Model):
    caterer     =   models.ForeignKey(Caterer, null=True,blank=True,on_delete=models.CASCADE)
    name        =   models.CharField(max_length=30)
    price       =   models.DecimalField(decimal_places=2, max_digits=20)
    description =   models.TextField()
    days_to_deliver =   models.PositiveSmallIntegerField(
        help_text="How many days will it take it to deliver the service.",
        validators=[
            MaxValueValidator(7),
            MinValueValidator(1)
        ])
    minimum_order_quantity = models.PositiveSmallIntegerField(
        help_text="What is the minimum order quantity you an accept?",
        validators=[
            MaxValueValidator(7),
            MinValueValidator(1)
        ]
    )
    rating      =   models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

def caterer_pre_save_reciever(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(caterer_pre_save_reciever,Caterer)