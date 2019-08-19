from django import forms
from .models import Pattern


class PatternForm(forms.ModelForm):

    class Meta:
        model = Pattern
        fields = ('pattern_text', 'output_text')

    def clean_pattern_text(self):
        value = self.cleaned_data['pattern_text']
        if len(value) < 1:
            raise forms.ValidationError(
                '%(min_length)s文字以上で入力してください', params={'min_length': 1})
        return value

    def clean_output_text(self):
        value = self.cleaned_data['output_text']
        if len(value) < 1:
            raise forms.ValidationError(
                '%(min_length)s文字以上で入力してください', params={'min_length': 1})
        return value
