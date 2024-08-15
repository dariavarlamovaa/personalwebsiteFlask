FROM python:3

COPY . /my_pwflask

WORKDIR /my_pwflask

EXPOSE 5001

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=main.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]