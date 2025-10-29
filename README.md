# dileep-todo-gcp

Full-stack Todo App (React frontend + FastAPI backend + MongoDB in GKE) — GitHub Actions CI/CD to GKE.

**What you get**
- backend/ : FastAPI service (async motor client)
- frontend/: React (Vite) app
- mongodb/: Kubernetes manifests to run MongoDB inside GKE (for demo)
- .github/workflows/: CI/CD workflows to build, push and deploy to GKE
- docker-compose.yml for local testing
- README with quick deploy steps below

**Quick deploy (summary)**
1. Create Git repo and push contents of this folder to `main` branch.
2. In GitHub repo > Settings > Secrets > Actions add:
   - `GCP_SA_KEY` : (service account JSON)
   - `GCP_PROJECT_ID` : modern-saga-472703-k3
   - `GCP_REGION` : us-central1
   - `GKE_CLUSTER` : test-demo-cluster
3. In Cloud Shell (optional) run:
   ```bash
   gcloud container clusters get-credentials test-demo-cluster --zone us-central1-a --project modern-saga-472703-k3
   kubectl apply -f mongodb/
   kubectl apply -f backend/k8s/
   kubectl apply -f frontend/k8s/
   ```
4. Or rely on GitHub Actions to build and deploy on push to main.
5. Get services and external IPs:
   ```bash
   kubectl get svc -A
   ```
