from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import  pre_save
from django.utils.text import slugify


class databank(models.Model):

    categories = (
        ('Buy & Sell', 'Buy & Sell'),
        ('Cars & Vehicles', 'Cars & Vehicles'),
        ('Real Estate', 'Real Estate'),
        ('Mobiles', 'Mobiles'),
        ('Furniture', 'Furniture'),
        ('Bikes', 'Bikes'),
        ('Jobs', 'Jobs'),
        ('Services', 'Services'),
        ('Community', 'Community'),
        ('Vacation Rentals', 'Vacation Rentals'),
    )
    title = models.CharField(max_length=100, verbose_name='Ad title', null=False)
    category = models.CharField(max_length=20, null=True, choices=categories, default='01', verbose_name='Select a category')
    content = models.TextField(max_length=400, null=True, verbose_name='Description')
    price = models.CharField( max_length=50,  null=True, verbose_name='Price (Be specific with currency type & amount)')
    location = models.CharField(max_length=100, null=True, verbose_name='Location')
    contact = models.IntegerField( null=True, verbose_name='Phone Number (Your phone number will show up on your Ad.)')
    email = models.EmailField(max_length=50, null=True, verbose_name='Email (Your email address will not be shared with others.)')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Posted')
    owner = models.CharField(max_length=17, null=True, verbose_name="Name of the owner")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Owner')
    photo = models.ImageField(upload_to='media', verbose_name='Photo')
    slug = models.SlugField(unique=True,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = databank.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=databank)