from django import forms
from django.contrib.staticfiles import finders
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Announcement


class AnnouncementForm(forms.Form):
    date_of_expiring = forms.DateField(label='', widget=forms.DateInput(attrs={'class': 'date', 'type': 'date', 'onchange' : 'preview_update(this, \'date\')'}), required=False)
    title = forms.CharField(label='', required=True, widget=forms.Textarea(attrs={'class': 'label-textarea', 'placeholder' : 'Заголовок объявления', 'onkeyup' : 'textarea_size(this); preview_update(this, \'title\')', 'cols' : 'none', 'rows' : 'none'}))
    body = forms.CharField(label='', required=True, widget=forms.Textarea(attrs={'class': 'label-textarea', 'onkeyup' : 'textarea_size(this); preview_update(this, \'descr\')', 'cols' : 'none', 'rows' : 'none'}))
    is_pinned = forms.BooleanField(label='Закрепить', required=False)
    image_url = forms.FilePathField(label='Выбрать обложку', path=finders.find("img/announcements/covers"), required=False, widget=forms.TextInput(attrs={'class': 'url-input'}))
    files = forms.FileField(label='Прикрепить файлы', widget=forms.FileInput(attrs={'class':"file-input", "id" : 'file', "multiple" : ''}), required=False)
    file_id_to_delete = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'fitd'}), required=False)

    def clean_date_of_expiring(self):
        exdate = self.cleaned_data.get('date_of_expiring')
        if exdate is not None and datetime.now().date() > exdate:
            raise ValidationError('Неверная дата')
