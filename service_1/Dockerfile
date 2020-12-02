FROM python:3.7

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV DB_URI=${DB_URI}
ENV KEY=${KEY}

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]