import random
#from django.test import TestCase
from .models import User, Settings, Category, Task
from random import randrange
from datetime import datetime
import pytz


def random_date():
    year = random.randint(2014, 2016)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)

    return datetime(year, month, day, hour, minute, tzinfo=pytz.utc)

counter = 1


def generate_random_user_data(username=None, password=None, cats=1, tasks=1):
    global counter

    r = counter
    username = username if username else 'user%s' % r
    password = password if password else 'pass%s' % r
    email = '%s@mail.com' % r

    u = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
    print('USER: %s, %s' % (username, password))
    u.save()

    s = Settings(user=u)
    print('SETTINGS: %s' % s)
    s.save()

    for i in range(cats):
        c = Category(user=u, name='%s_cat_%s' % (username, i))
        print('CATEGORY: %s' % c)
        c.save()

        for i in range(tasks):
            t = Task(category=c,
                     user=u,
                     name='%s_task_%s' % (username, i),
                     started=random_date(),
                     duration=random.randint(1, 30)
                     )
            print('TASK: %s' % t)
            t.save()

    counter += 1
