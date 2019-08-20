from django import forms
from .models import Pattern


class PatternForm(forms.ModelForm):

    class Meta:
        model = Pattern
        fields = ('pattern_text', 'output_text')

    def clean_pattern_text(self):
        ptn_txt = self.cleaned_data['pattern_text']
        if len(ptn_txt) < 1:
            raise forms.ValidationError(
                '%(min_length)s文字以上で入力してください', params={'min_length': 1})
        return ptn_txt

    def clean_output_text(self):
        op_txt = self.cleaned_data['output_text']
        if len(op_txt) < 1:
            raise forms.ValidationError(
                '%(min_length)s文字以上で入力してください', params={'min_length': 1})
        return op_txt

    def clean(self):
        ptn_txt = self.cleaned_data.get('pattern_text')
        p_flt = Pattern.objects.filter(user__username=self.user)
        for p in p_flt:
            if p.pattern_text == ptn_txt:
                raise forms.ValidationError('￿入力されたパターンは既に登録済みです')
        super().clean()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PatternForm, self).__init__(*args, **kwargs)

