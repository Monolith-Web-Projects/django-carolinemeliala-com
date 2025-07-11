# Use the official lightweight PostgreSQL image
FROM postgres:15-alpine

# Install optional client tools
RUN apk add --no-cache \
    bash \
    curl \
    nano \
    bind-tools \
    postgresql-client

# Optional: preload SQL or shell init scripts
# COPY ./initdb /docker-entrypoint-initdb.d/

# Set default environment variables
ENV POSTGRES_DB=postgres \
    POSTGRES_USER=django \
    POSTGRES_PASSWORD=secretpassword

EXPOSE 5432