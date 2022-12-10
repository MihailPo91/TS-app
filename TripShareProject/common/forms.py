from django import forms

from TripShareProject.common.models import Comment, Rating


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Add comment...', 'rows': 2, 'cols': 50
            })
        }


class RatingForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=Rating.RATING_CHOICES)
    comment = forms.Textarea()

    class Meta:
        model = Rating
        fields = ['rating', 'comment']
        widgets = {'comment': forms.Textarea(attrs={
            'rows': 5
        })}

