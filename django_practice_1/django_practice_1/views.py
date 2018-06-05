from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Use /hello-world URL
def hello_world(request):
    """Return a 'Hello World' string using HttpResponse"""
    return HttpResponse('Hello World')
    pass


# Use /date URL
def current_date(request):
    """
        Return a string with current date using the datetime library.

        i.e: 'Today is 5, January 2018'
    """
    todays_date = datetime.now()
    return HttpResponse("Today is {}".format(todays_date.strftime("%d, %B %Y")))
    pass


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    """
        Return a string with the format: 'Your age is X years old'
        based on given /year/month/day datetime that come in the URL.

        i.e: /my-age/1992/1/20 returns 'Your age is 26 years old'
    """
    todays_date = datetime.now()
    age = todays_date.year - year
    
    return HttpResponse('Your age is {} years old'.format(age))
    
    pass


# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    """
        Return a string with the format: 'Days until next birthday: XYZ'
        based on a given string GET parameter that comes in the URL, with the
        format 'YYYY-MM-DD'
    """
    bday =  datetime.strptime(birthday,"%Y-%m-%d")
    todays_date = datetime.now()
    

    year = todays_date.year
    if todays_date.month > bday.month:
        year = todays_date.year + 1
    elif  todays_date.month == bday.month:
        if todays_date.day >= bday.day:
            year = todays_date.year + 1

    print(year)
    n_bday = datetime.strptime("{}-{}-{}".format(year,bday.month,bday.day),"%Y-%m-%d")
    time_tobday = n_bday - todays_date
    return HttpResponse('Days until next birthday: {}'.format(abs(time_tobday.days)))

    

# Use /profile URL
def profile(request):
    """
        Render the 'profile.html' sending the context given below, using the
        'render' function imported from Django.
        Make sure to replace the values inside the template in the proper places.
    """
    
    return render(request,"profile.html",{'author':'Apple' , 'age':42})    
pass



"""
    The goal for next task is to practice routing between two URLs.
    You will have:
        - /authors --> contains a list of Authors (template is provided to you)
        - /author/<authors_last_name> --> contains the detail for given author,
        using the AUTHORS_INFO provided below.

    First view just have to render the given 'authors.html' template sending the
    AUTHORS_INFO as context.

    Second view has to take the authors_last_name provided in the URL, look for
    for the proper author info in the dictionary, and send it as context while
    rendering the 'author.html' template. Make sure to complete the given
    'author.html' template with the data that you send.
"""
AUTHORS_INFO = {
    'poe': {
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
    },
    'borges': {
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1899',
    }
}

# Use provided URLs, don't change them
def authors(request):
    return render(request,"authors.html",AUTHORS_INFO)



def author(request, authors_last_name):
    return render(request,"author.html",AUTHORS_INFO[authors_last_name])

