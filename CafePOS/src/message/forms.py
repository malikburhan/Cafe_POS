from django import forms


# Register your forms here.
class MobileConnectionForm(forms.Form):
    ip = forms.CharField(max_length=15)
    port = forms.CharField(max_length=4)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ip'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter IP', 'value': '192.168.10.7'})
        self.fields['port'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Port', 'value': '2333'})


class OutBoxForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Message', 'row': 4})