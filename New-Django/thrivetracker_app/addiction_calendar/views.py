from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event
from .forms import VenueForm

def add_venue(request):
    submitted = request.GET.get('submitted', False)
    form = None

    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
        else:
            submitted = True 
    if form is None:
        form = VenueForm()
    return render(request, 'addiction_events/add_venue.html', {'form': form, 'submitted': submitted})

def all_events(request):
    events_list = Event.objects.all()
    return render(request, 'addiction_events/events_list.html',
            {'events_list': events_list})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # the {} is called a context dictionary
    # it allows us to pass from the front end to the back end
    # and vice versa
    name = "Addiction Calendar"
    # convert month name to number
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    # get current year
    now = datetime.now()
    current_year = now.year

    # get current time
    current_time = now.strftime("%I:%M %p")

    return render(request, 'addiction_events/home.html', {
        'name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'current_year': current_year,
        'current_time': current_time,
        })