
"""
Peter can see a clock in the mirror from the place he sits in the office. When he saw the clock shows 12:22
He knows that the time is 11:38

in the same manner:

05:25 --> 06:35

01:50 --> 10:10

11:58 --> 12:02

12:01 --> 11:59

Please complete the function WhatIsTheTime(timeInMirror), where timeInMirror is the mirrored time (what Peter sees) as string.

Return the real time as a string.

Consider hours to be between 1 <= hour < 13.

So there is no 00:20, instead it is 12:20.

There is no 13:20, instead it is 01:20.
"""


def what_is_the_time(time_in_mirror):
    hr = int(time_in_mirror[:2])
    min = int(time_in_mirror[-2:])

    reversed_min = 30-(min-30) if min >= 30 else (30-min)+30

    if min == 0: return '%02d:00'%(12-hr or 12)
    if hr == 12 : return '%02d:%02d'%(11, reversed_min)
    return '%02d:%02d'%(11-hr or 12, reversed_min)



"""
Clever
"""

def what_is_the_time(time_in_mirror):
    h, m = map(int, time_in_mirror.split(':'))
    return '{:02}:{:02}'.format(-(h + (m != 0)) % 12 or 12, -m % 60)
