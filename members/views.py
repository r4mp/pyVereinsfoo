from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.views.generic import DetailView, ListView

import logging
logger = logging.getLogger('pyVereinsfoo.members.views')

from members.models import Member

# Create your views here.

@login_required
def create(request):
    pass

def search(request):
    if request.method == "POST":
        search_string = request.POST['search_string']
    else:
        search_string = ''

    members = Member.objects.filter(first_name__contains=search_string)
    logger.debug('search')

    return render_to_response('members/search.html', {'members': members},
            context_instance=RequestContext(request))

#def index(request):
#    members = Member.objects.all()
#    return render_to_response('members/index.html', {'object_list': members},
#        context_instance=RequestContext(request))

#def detail(request, slug):
#    member = get_object_or_404(Member, slug=slug)
#    return render_to_response('members/detail.html', {'object': member},
#        context_instance=RequestContext(request))

class MemberListView(ListView):
    template_name = 'members/index.html'

    def get_queryset(self):
        members = Member.objects.all()
        logger.debug('No. of members: %d' % members.count())
        return members


class MemberDetailView(DetailView):
    model = Member
    template_name = 'members/detail.html'
