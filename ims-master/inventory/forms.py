from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('ip_address', 'info', 'hostname', 'able_to_ping', 'able_to_login',
                  'physical_or_vm', 'issues', 'type')


class WindowsForm(forms.ModelForm):
    class Meta:
        model = Windows
        fields = ('ip_address', 'info', 'hostname', 'able_to_ping', 'able_to_login',
                  'physical_or_vm', 'issues', 'type')


class LinuxForm(forms.ModelForm):
    class Meta:
        model = Linux
        fields = ('ip_address', 'info', 'hostname', 'able_to_ping', 'able_to_login',
                  'physical_or_vm', 'issues', 'type')


class NetworkForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = ('ip_address', 'info', 'hostname', 'able_to_ping', 'able_to_login',
                  'physical_or_vm', 'issues', 'type')
