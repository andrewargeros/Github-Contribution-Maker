import pyautogui
import random
import time

def str_time_prop(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)

time.sleep(5)

pyautogui.typewrite("""cd C:/RScripts/contribution-dump
""")
time.sleep(1)
pyautogui.typewrite('git init')

for i in range(30):
   date = random_date("2021-06-19", "2021-06-25", random.random())

   message = f"""git commit --allow-empty --date "{date}" -m "{date}"
   git push
   """
   pyautogui.typewrite(message)
