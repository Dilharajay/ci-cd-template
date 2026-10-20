# FastAPI + uv + Docker starter

A small project template for developing with `uv`, running locally or in Docker, and using GitHub Actions for checks and image publishing.

## Start locally

```bash
uv sync
uv run uvicorn src.main:app --reload
```

Open <http://127.0.0.1:8000/health> or the interactive API docs at <http://127.0.0.1:8000/docs>.

uv.lock is required to run the project. If you don't have it, run `uv sync` to generate it.

## Build and run the container

```bash
docker build -t fastapi-uv-template:local .
docker run --rm -p 8000:8000 fastapi-uv-template:local
```

Visit <http://localhost:8000/health>.

## GitHub workflow

The workflow in `.github/workflows/ci.yml` runs `uv sync` and `pytest` on pushes and pull requests to `main`, then builds a Docker image. Pushing a version tag such as `v1.0.0` also publishes the image to GitHub Container Registry (`ghcr.io/<owner>/<repo>`). Enable GitHub Actions package write access if your repository requires it.

Typical release sequence:

```bash
git switch -c feat/my-change
# edit files
uv lock
git add .
git commit -m "Add my change"
git push -u origin feat/my-change
# Open a pull request; merge after CI passes.
git switch main
git pull
git tag v1.0.0
git push origin v1.0.0
```

## Adapt it

- Change the project name in `pyproject.toml`.
- Change `main:app` in the Dockerfile if your ASGI app lives elsewhere (for example, `app.main:app`).
- Add runtime configuration through environment variables; keep secrets out of Git and the image.
- For Kubernetes, use the published versioned image tag in your Deployment.

