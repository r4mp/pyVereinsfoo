from django.forms import ModelForm
from django.template.defaultfilters import slugify

from members.models import Member

class MemberForm(ModelForm):

    class Meta:
        model = Member
        exclude = ('slug', 'date_created', 'date_updated', 'created_by')

    def __init__(self, **kwargs):
        self.__user = kwargs.pop('user', None)
        super(MemberForm, self).__init__(**kwargs)

    def save(self, commit=True):
    
        if self.instance.pk is None:
            if self.__user is None:
                raise TypeError("You didn't give an user argument to the constructor.")
    
            self.instance.slug = slugify(self.instance.title)
            self.instance.author = self.__user
    
        return super(MemberForm, self).save(commit)
