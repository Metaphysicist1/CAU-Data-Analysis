# CAU-Data-Analysis

A Flask web app that queries Google BigQuery's public dataset (`google_analytics_sample`) and displays user engagement metrics, containerized with Docker.

## Setup Instructions

1. **Prerequisites**:

   - Google Cloud project with BigQuery API enabled.
   - Service account key (JSON) downloaded as `service_account_key.json`.
   - Docker and Docker Compose installed.

2. **Project Setup**:

   - Place `service_account_key.json` in the project root.
   - Ensure the service account has BigQuery access (e.g., `BigQuery Data Viewer` role).

3. **Build and Run**:
   ```bash
   docker-compose up --build
   ```
