
FROM python:3.8.10

ADD requirements.txt /requirements.txt
ADD billboard.py /billboard.py
ADD config.py /config.py

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "/billboard.py"]
