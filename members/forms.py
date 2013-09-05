from django.forms import ModelForm

from members.models import Member

class MemberForm(ModelForm):
    class Meta:
        model = Member
        exclude = ('slug', 'date_created', 'date_updated', 'created_by')
