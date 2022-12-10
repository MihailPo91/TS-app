from django import forms

from TripShareProject.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['owner', ]
        widgets = {
            'description': forms.Textarea()
        }


class PhotoEditForm(PhotoCreateForm):
    class Meta:
        model = Photo
        exclude = ['owner', 'photo', ]
        widgets = {
            'description': forms.Textarea()
        }
