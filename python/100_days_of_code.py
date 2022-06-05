from datetime import date


DELTA = date.today() - date(2022, 3, 1)

if (DELTA.days < 101):
    print(f"Today is day {DELTA.days}")

else:
    print('100 Days of Code sprint has ended')
