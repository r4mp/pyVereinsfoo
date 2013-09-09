from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render

from django.views.generic import DetailView, ListView
from members.forms import MemberForm

import logging
logger = logging.getLogger('pyVereinsfoo.members.views')

from members.models import Member

# Create your views here.

@login_required
def create(request):
    logger.debug('create')
    if request.method == 'POST':
        form = MemberForm(data = request.POST)
        if form.is_valid():
            member = form.save()
            return HttpResponseRedirect(member.get_absolute_url())
    else:
        form = MemberForm()

    return render(request, 'members/form.html', 
        { 'form' : form, 'create' : True })

@login_required
def edit(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    #if member.author != request.user and not request.user.is_staff:
    #    return HttpResponseForbidden()
    if request.method == 'POST':
        form = MemberForm(instance=member, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(member.get_absolute_url())
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/form.html',
        {'form': form, 'create': False, 'object': member})
        
@login_required
def search(request):
    if request.method == "POST":
        search_string = request.POST['search_string']
    else:
        search_string = ''

    logger.debug(search_string)
    members = Member.objects.filter(first_name__contains=search_string)
    logger.debug('search')

    return render(request, 'members/search.html', { 'members': members, 'searchstring' : search_string })

#@login_required
#def index(request):
#    members = Member.objects.all()
#    return render_to_response('members/index.html', {'object_list': members},
#        context_instance=RequestContext(request))

#@login_required
#def detail(request, slug):
#    member = get_object_or_404(Member, slug=slug)
#    return render_to_response('members/detail.html', {'object': member},
#        context_instance=RequestContext(request))

#@login_required
class MemberListView(ListView):
    template_name = 'members/index.html'

    def get_queryset(self):
        members = Member.objects.all()
        logger.debug('No. of members: %d' % members.count())
        return members

#@login_required
class MemberDetailView(DetailView):
    model = Member
    template_name = 'members/detail.html'
