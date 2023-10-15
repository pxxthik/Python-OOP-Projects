import yagmail
import pandas
from news import NewsFeed
import datetime

df = pandas.read_excel("people.xlsx")

for index, row in df.iterrows():
    today = datetime.datetime.now()
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=(today - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
                         to_date=today.strftime("%Y-%m-%d"))

    email = yagmail.SMTP(user="pythonprocourse1@gmail.com",
                         password="python_pro_course_1")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']},\n See what's on about {row['interest']} today.\n{news_feed.get()}")
