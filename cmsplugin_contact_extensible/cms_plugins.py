from django import forms
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool

from cmsplugin_contact.cms_plugins import ContactPlugin
from .models import CustomContact
from .forms import CustomContactForm

from unidecode import unidecode

class CustomContactPlugin(ContactPlugin):
    name = _("Custom Contact Form")
    
    model = CustomContact
    contact_form = CustomContactForm
    
    render_template = "cmsplugin_contact_extensible/contact.html"
    email_template = "cmsplugin_contact_extensible/email.txt"
    subject_template = "cmsplugin_contact_extensible/subject.txt"
    
    change_form_template = "cmsplugin_contact_extensible/admin/plugin_change_form.html"
    
    fieldsets = (
        (None, {
                'fields': ('site_email', 'email_label',
                           'subject_label', 'content_label', 'thanks',
                           'submit',),
        }),
        (_('Attachment'), {
                'fields': ('allow_attachment',)
        }),
        (_('Extra fields'), {
                'fields': ('extra_fields',)
        }),
        (_('Spam Protection'), {
                'fields': ('spam_protection_method', 'akismet_api_key',
                           'recaptcha_public_key', 'recaptcha_private_key',
                           'recaptcha_theme')
        })
    )
    
    def create_form(self, instance, request):
        form = ContactPlugin.create_form(self, instance, request)
        for field_name in instance.extra_fields.split(','):
            form.fields["extra_field_%s" % unidecode(field_name)] = forms.CharField(label=field_name)
        
        return form

plugin_pool.register_plugin(CustomContactPlugin)