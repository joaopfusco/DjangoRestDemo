FROM python:3.13-alpine

RUN mkdir -p /app
WORKDIR /app
COPY . .

RUN python -m pip install -r requirements.txt
RUN chmod +x entrypoint.sh

EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]
CMD ["python", "-m", "uvicorn", "DjangoRestDemo.asgi:application", "--host", "0.0.0.0", "--port", "8000"]