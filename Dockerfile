FROM python:3.12-alpine as builder

RUN mkdir -p /app
WORKDIR /app
COPY . .

ENV PIPENV_VENV_IN_PROJECT=1

RUN python -m pip install pipenv
RUN pipenv install

FROM python:3.12-alpine

COPY --from=builder /app /app
WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

RUN chmod +x entrypoint.sh

EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]

CMD ["python", "-m", "uvicorn", "DjangoRestDemo.asgi:application", "--host", "0.0.0.0", "--port", "8000"]