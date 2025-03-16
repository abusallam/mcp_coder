#!/bin/bash

HEALTH_URL="http://localhost:8000/api/v1/health"
MAX_RETRIES=5
RETRY_INTERVAL=10

for i in $(seq 1 $MAX_RETRIES); do
    response=$(curl -s -o /dev/null -w "%{http_code}" $HEALTH_URL)
    if [ $response -eq 200 ]; then
        echo "Service is healthy"
        exit 0
    fi
    echo "Attempt $i: Service not healthy yet, waiting..."
    sleep $RETRY_INTERVAL
done

echo "Service failed to become healthy"
exit 1
