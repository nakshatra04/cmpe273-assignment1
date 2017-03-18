FROM python:2.7.13
MAINTAINER Nakshatra "nakshatra@sjsu.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
CMD ["app.py", arg1]