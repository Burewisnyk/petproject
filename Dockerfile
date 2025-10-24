# syntax=docker/dockerfile:1
# Docker Buildkit is required to build this Dockerfile

FROM python:3.12-slim

# Install git (required for uv to fetch Git dependencies)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create a enviroment variable for application
ENV PATH="/app/.venv/bin:$PATH"

# Compile bytecode
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#compiling-bytecode
ENV UV_COMPILE_BYTECODE=1

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app

# Install the application dependencies.
RUN uv sync --frozen --no-cache --no-dev

# Run the application.
CMD ["/app/", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]