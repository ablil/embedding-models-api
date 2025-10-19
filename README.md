# Text Embedder

Lightweight Flask service that exposes a single endpoint to compute sentence embeddings
using `sentence-transformers` (default model: `sentence-transformers/all-MiniLM-L6-v2`).

The repository includes a `Dockerfile` and `compose.yml` for easy containerized deployment and model caching.


## Get started
```bash
docker compose -f compose.yml up --build
```

A prebuilt image is published to Github container registry on push to **main** branch.

Pull and run the image immediately:
```bash
docker pull ghcr.io/ablil/embedding-models-api:latest
docker run -p 8000:8000 ghcr.io/ablil/embedding-models-api:latest
```

## API

* POST /embed 
  * Request JSON: { "text": "single string or array of strings" }
  * Response JSON: { "embeddings": [[...], [...]] } — list of embedding vectors (floats)
* GET /health 
    * Response JSON: { "status": "ok" }