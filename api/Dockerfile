FROM breqwatr/applib:latest
ADD api /app/api
RUN pip install /app/api

CMD gunicorn appapi.main:app --bind 0.0.0.0:80

