# Tag name env var is the name of the version
docker build -t us-central1-docker.pkg.dev/glbt-challenge-migrations/bq-glbt-migrator-images/bq-glbt-migrator:${TAG_NAME} .
docker push us-central1-docker.pkg.dev/glbt-challenge-migrations/bq-glbt-migrator-images/bq-glbt-migrator:${TAG_NAME}