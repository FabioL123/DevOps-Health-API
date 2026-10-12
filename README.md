Original path: devops-health-api/README.md
Note: this PDF displays the file's text. It is not a runnable replacement for the original .py, .sql, .yml, or configuration file.
# DevOps Health API
A minimal Flask API packaged in Docker. It includes `/health` and `/version` endpoints, automated tests,
a non-root container user, a container health check, and a GitHub Actions CI workflow.
## Run locally
Python 3.10+ recommended.
```bash
python -m venv .venv
source .venv/bin/activate # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m app.main
```
Open `http://127.0.0.1:8000/health`, `http://127.0.0.1:8000/version`, or run tests:
```bash
python -m pytest -q
```
## Run with Docker
```bash
docker build -t devops-health-api:1.0.0 .
docker run --rm -p 8000:8000 -e APP_VERSION=1.0.0 devops-health-api:1.0.0
```
Then check `http://127.0.0.1:8000/health`.
## DevOps concepts demonstrated
- Reproducible dependency installation
- Automated test workflow on push and pull request
- Container image build and health check
- Non-root runtime user and slim base image
- Environment-based configuration
This is a demo service, not a production deployment. A real production service would also need
deployment configuration, logging/metrics, secret management, and security review.
