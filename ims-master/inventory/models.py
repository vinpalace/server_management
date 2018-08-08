from django.db import models


class Product(models.Model):
    ip_address = models.CharField(max_length=200, blank=True, null=True, default='0.0.0.0')
    info = models.CharField(max_length=200, blank=True, null=True, default=' ')
    hostname = models.CharField(max_length=200, blank=True, null=True, default=' ')
    able_to_ping = models.CharField(max_length=200, blank=True,null=True, default=' ')
    able_to_login = models.CharField(max_length=200,blank=True, null=True, default=' ')
    physical_or_vm = models.CharField(max_length=200, blank=True,null=True, default=' ')
    issues = models.CharField(max_length=200, blank=True,null=True, default='None')
    status = models.CharField(max_length=6, default='False', blank=False, null=False)
    type = models.CharField(max_length=200, blank=True, null=True, default='NaN')

    def __str__(self):
        return 'Id:{0} Name:{1}'.format(self.hostname, self.ip_address)


class Windows(models.Model):
    ip_address = models.CharField(max_length=200, blank=True, null=True, default='0.0.0.0')
    info = models.CharField(max_length=200, blank=True, null=True, default=' ')
    hostname = models.CharField(max_length=200, blank=True, null=True, default=' ')
    able_to_ping = models.CharField(max_length=200, blank=True,null=True, default=' ')
    able_to_login = models.CharField(max_length=200,blank=True, null=True, default=' ')
    physical_or_vm = models.CharField(max_length=200, blank=True,null=True, default=' ')
    issues = models.CharField(max_length=200, blank=True,null=True, default='None')
    status = models.CharField(max_length=6, default='False', blank=False, null=False)
    type = models.CharField(max_length=200, blank=True, null=True, default='NaN')

    def __str__(self):
        return 'Id:{0} Name:{1}'.format(self.hostname, self.ip_address)


class Linux(models.Model):
    ip_address = models.CharField(max_length=200, blank=True, null=True, default='0.0.0.0')
    info = models.CharField(max_length=200, blank=True, null=True, default=' ')
    hostname = models.CharField(max_length=200, blank=True, null=True, default=' ')
    able_to_ping = models.CharField(max_length=200, blank=True,null=True, default=' ')
    able_to_login = models.CharField(max_length=200,blank=True, null=True, default=' ')
    physical_or_vm = models.CharField(max_length=200, blank=True,null=True, default=' ')
    issues = models.CharField(max_length=200, blank=True,null=True, default='None')
    status = models.CharField(max_length=6, default='False', blank=False, null=False)
    type = models.CharField(max_length=200, blank=True, null=True, default='NaN')

    def __str__(self):
        return 'Id:{0} Name:{1}'.format(self.hostname, self.ip_address)


class Network(models.Model):
    ip_address = models.CharField(max_length=200, blank=True, null=True, default='0.0.0.0')
    info = models.CharField(max_length=200, blank=True, null=True, default=' ')
    hostname = models.CharField(max_length=200, blank=True, null=True, default=' ')
    able_to_ping = models.CharField(max_length=200, blank=True,null=True, default=' ')
    able_to_login = models.CharField(max_length=200,blank=True, null=True, default=' ')
    physical_or_vm = models.CharField(max_length=200, blank=True,null=True, default=' ')
    status = models.CharField(max_length=6, default='False', blank=False, null=False)
    issues = models.CharField(max_length=200, blank=True,null=True, default='None')
    type = models.CharField(max_length=200, blank=True, null=True, default='NaN')

    def __str__(self):
        return 'Id:{0} Name:{1}'.format(self.hostname, self.ip_address)
