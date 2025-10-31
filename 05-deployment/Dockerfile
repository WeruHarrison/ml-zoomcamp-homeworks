FROM agrigorev/zoomcamp-model:2025

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN pip install uvicorn

WORKDIR /app

COPY ".python-version" "pyproject.toml" "uv.lock" "./"

RUN uv sync --locked

ENV PATH="/app/.venv/bin:$PATH"

COPY "conversion.py" "pipeline_v1.bin" "./"

EXPOSE 9696

ENTRYPOINT ["uvicorn", "conversion:app", "--host", "0.0.0.0", "--port", "9696"]