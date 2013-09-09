# encoding: utf-8
from django.db import models
from django.utils.timezone import now

# Create your models here.

class Address(models.Model):
    """Address model."""
    street = models.CharField(u'street', max_length=100)
    zip_code = models.CharField(u'zip', max_length=10)
    city = models.CharField(u'city', max_length=100)
    country = models.CharField(u'country', max_length=100)
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False)
    #slug = models.SlugField(unique=True)
    created_by = models.CharField(u'username', max_length=100)

    class Meta:
        verbose_name = u'Address'
        verbose_name_plural = u'Addresses'

    def __unicode__(self):
        return self.street + ", " + self.zip_code + " " + self.city

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
            self.date_updated = now()
        super(Address, self).save(*args, **kwargs)

class Member(models.Model):
    """Member model."""
    member_id = models.CharField(primary_key=True, max_length=100)
    first_name = models.CharField(u'first name', max_length=100)
    last_name = models.CharField(u'last name', max_length=100)
    private_address = models.OneToOneField(Address)
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False)
    slug = models.SlugField(unique=True)
    created_by = models.CharField(u'username', max_length=100)
    #client = models.OneToOneField(Client)

    class Meta:
        verbose_name = u'Member'
        verbose_name_plural = u'Members'

    def __unicode__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        # TODO !!! --> Funktioniert natuerlich nicht mehr, da member_id ja gesetzt wird
        #if not self.member_id:
        self.date_created = now()
        self.date_updated = now()
        super(Member, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('members_member_detail', (), {'slug': self.slug})
