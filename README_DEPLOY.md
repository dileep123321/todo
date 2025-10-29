# Deploy details

1. Create Git repo and push code to GitHub `main` branch.
2. In repo settings -> Secrets -> Actions add:
   - GCP_SA_KEY (service account JSON)
   - GCP_PROJECT_ID = modern-saga-472703-k3
   - GCP_REGION = us-central1
   - GKE_CLUSTER = test-demo-cluster
   - GKE_ZONE = us-central1-a
3. Push to main -> GitHub Actions will build images and apply manifests to cluster.
4. To manually run in Cloud Shell:
   gcloud container clusters get-credentials test-demo-cluster --zone us-central1-a --project modern-saga-472703-k3
   kubectl apply -f mongodb/
   kubectl apply -f backend/k8s/
   kubectl apply -f frontend/k8s/
   kubectl get svc -A
