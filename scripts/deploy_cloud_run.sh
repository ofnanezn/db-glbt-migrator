gcloud run deploy ${SERVICE_NAME} \
    --project=${PROJECT_ID} \
    --region=us-central1 \
    --image=us-central1-docker.pkg.dev/glbt-challenge-migrations/bq-glbt-migrator-images/bq-glbt-migrator:${TAG_NAME} \
    --allow-unauthenticated \
    --max-instances=3 \
    --service-account=${DEFAULT_SA} \
    --port=8080 \
    --env-vars-file="config/env-vars.yaml"