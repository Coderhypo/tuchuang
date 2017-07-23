FROM python:3.6

RUN mkdir /tuchuang
COPY . /tuchuang
WORKDIR /tuchuang

RUN pip install -r requirements.txt
CMD python app_run.py

EXPOSE 8888