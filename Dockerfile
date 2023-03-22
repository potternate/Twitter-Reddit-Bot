FROM python:3.8.10

ADD requirements.txt /requirements.txt
ADD tweetJob.py /tweetJob.py
ADD config.py /config.py
ADD customFeed.py /customFeed.py

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "/tweetJob.py"]
