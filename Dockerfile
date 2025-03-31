FROM python:3.12-alpine AS builder

RUN mkdir -p /app
WORKDIR /app
COPY . .

RUN apk add --no-cache gcc musl-dev libpq-dev

RUN python -m pip install --no-cache-dir pdm
RUN pdm install --prod --no-lock --no-editable

FROM python:3.12-alpine

COPY --from=builder /app /app
WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

RUN chmod +x entrypoint.sh

EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]

CMD ["python", "-m", "uvicorn", "DjangoRestDemo.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
