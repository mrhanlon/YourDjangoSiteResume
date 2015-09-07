"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Matthew R Hanlon',
    'bio' : 'I\'m a engineer at the Texas Advanced Computing Center!',
    'email' : 'mrhanlon@tacc.utexas.edu', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'mattorantimatt', # No @ symbol, just the handle.
    'github_username' : "mrhanlon",
    'headshot_url' : 'https://s.gravatar.com/avatar/157f788c372e1f39c88a9b6f5b9dd33d?size=256&default=retro', # Link to your GitHub, Twitter, or Gravatar profile image.
}

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,
                'year': datetime.now().year,
            })
    )