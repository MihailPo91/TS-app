from django import forms

from TripShareProject.landmarks.models import Landmark


class LandmarkCreateForm(forms.ModelForm):
    class Meta:
        model = Landmark
        fields = '__all__'
        widgets = {
            'description': forms.Textarea()
        }


class LandmarkEditForm(LandmarkCreateForm):
    class Meta:
        model = Landmark
        fields = '__all__'
        widgets = {
            'description': forms.Textarea()
        }


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Search for a landmark...'
        })
    )
