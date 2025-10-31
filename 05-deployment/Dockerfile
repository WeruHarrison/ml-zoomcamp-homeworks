FROM agrigorev/zoomcamp-model:2025

RUN pip install uv

WORKDIR /app

ENV PATH="/code/.venv/bin:$PATH"

COPY ".python-version" "pyproject.toml" "uv.lock" ./

RUN uv sync --locked

COPY "predict.py" "test_client.py" "conversion.py" "pipeline_v1.bin" ./

EXPOSE 9696

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]