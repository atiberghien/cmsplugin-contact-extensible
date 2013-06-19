from django import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from cmsplugin_contact.forms import ContactForm
from django.utils import simplejson as json

class CustomContactForm(ContactForm):
    attachment = forms.FileField(required=False)
    extra_fields = forms.CharField()
    
    def extra_field_list(self):
        for name in self.fields:
            if name.startswith('extra_field_'):
                yield(self[name])

    def clean_attachment(self):
        attachment = self.cleaned_data['attachment']
        if attachment:
            content_type = attachment.content_type
            if content_type in settings.ALLOWED_CONTACTFORM_MIMETYPES:
                if attachment.size > (settings.MAX_UPLOAD_CONTACTFORM_SIZE * 1024 * 1024):
                    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(attachment._size)))
            else:
                raise forms.ValidationError(_('File type is not supported'))
        
        return attachment
    
    def clean_extra_fields(self):
        extra_fields = self.cleaned_data['extra_fields']
        return json.loads(extra_fields)
        