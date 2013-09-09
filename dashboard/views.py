from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.shortcuts import render

import logging
logger = logging.getLogger('pyVereinsfoo.dashboard.views')

#from dashboard.models import Dashboard

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html', {})
