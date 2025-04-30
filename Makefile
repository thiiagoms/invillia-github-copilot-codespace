# Run tests with pytest
test:
    PYTHONPATH=/workspaces/invillia-github-copilot-codespace pytest tests/

# Install dependencies
install:
    pip3 install -r requirements.txt

# Lint Python code
lint:
    flake8 src/ tests/

# Run the FastAPI application
run:
    uvicorn src.app:app --reload --host 0.0.0.0 --port 8000