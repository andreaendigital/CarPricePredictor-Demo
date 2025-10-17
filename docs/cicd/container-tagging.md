# Container Image Tagging Examples

## Overview

Our CI/CD pipeline uses strategic container image tagging to manage deployments across different environments and track versions effectively.

## Tagging Strategy

### Production Tags
```yaml
# Main branch - Production releases
ghcr.io/andreaendigital/carprice-backend:latest
ghcr.io/andreaendigital/carprice-backend:v1.2.3
ghcr.io/andreaendigital/carprice-backend:prod-2024-01-15

ghcr.io/andreaendigital/carprice-frontend:latest
ghcr.io/andreaendigital/carprice-frontend:v1.2.3
ghcr.io/andreaendigital/carprice-frontend:prod-2024-01-15
```

### Development Tags
```yaml
# Develop branch - Staging releases
ghcr.io/andreaendigital/carprice-backend:develop
ghcr.io/andreaendigital/carprice-backend:dev-2024-01-15
ghcr.io/andreaendigital/carprice-backend:staging-latest

ghcr.io/andreaendigital/carprice-frontend:develop
ghcr.io/andreaendigital/carprice-frontend:dev-2024-01-15
ghcr.io/andreaendigital/carprice-frontend:staging-latest
```

### Feature Branch Tags
```yaml
# SCRUM branches - Feature testing
ghcr.io/andreaendigital/carprice-backend:scrum-96-docs
ghcr.io/andreaendigital/carprice-backend:feature-ml-enhancement
ghcr.io/andreaendigital/carprice-backend:sha-a1b2c3d

ghcr.io/andreaendigital/carprice-frontend:scrum-96-docs
ghcr.io/andreaendigital/carprice-frontend:feature-ui-update
ghcr.io/andreaendigital/carprice-frontend:sha-a1b2c3d
```

## GitHub Actions Implementation

### Tag Generation Logic
```yaml
- name: Generate Tags
  id: tags
  run: |
    BRANCH=${GITHUB_REF#refs/heads/}
    SHA=${GITHUB_SHA::7}
    DATE=$(date +%Y-%m-%d)

    if [[ "$BRANCH" == "main" ]]; then
      echo "tags=latest,prod-$DATE,sha-$SHA" >> $GITHUB_OUTPUT
    elif [[ "$BRANCH" == "develop" ]]; then
      echo "tags=develop,staging-latest,dev-$DATE" >> $GITHUB_OUTPUT
    elif [[ "$BRANCH" == SCRUM-* ]]; then
      CLEAN_BRANCH=$(echo $BRANCH | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]/-/g')
      echo "tags=$CLEAN_BRANCH,sha-$SHA" >> $GITHUB_OUTPUT
    else
      echo "tags=sha-$SHA" >> $GITHUB_OUTPUT
    fi
```

### Docker Build and Push
```yaml
- name: Build and Push Backend
  uses: docker/build-push-action@v4
  with:
    context: ./backend
    push: true
    tags: |
      ghcr.io/andreaendigital/carprice-backend:${{ steps.tags.outputs.tags }}
    labels: |
      org.opencontainers.image.source=${{ github.server_url }}/${{ github.repository }}
      org.opencontainers.image.revision=${{ github.sha }}
      org.opencontainers.image.created=${{ steps.date.outputs.date }}
```

## Tag Usage Examples

### Deployment Commands
```bash
# Production deployment
docker pull ghcr.io/andreaendigital/carprice-backend:latest
docker pull ghcr.io/andreaendigital/carprice-frontend:latest

# Staging deployment
docker pull ghcr.io/andreaendigital/carprice-backend:develop
docker pull ghcr.io/andreaendigital/carprice-frontend:develop

# Feature testing
docker pull ghcr.io/andreaendigital/carprice-backend:scrum-96-docs
docker pull ghcr.io/andreaendigital/carprice-frontend:scrum-96-docs
```

### Docker Compose Integration
```yaml
version: '3.8'
services:
  backend:
    image: ghcr.io/andreaendigital/carprice-backend:${TAG:-latest}
    ports:
      - "5002:5002"

  frontend:
    image: ghcr.io/andreaendigital/carprice-frontend:${TAG:-latest}
    ports:
      - "3000:3000"
```

## Registry Management

### Image Cleanup Policy
```yaml
# Keep last 10 versions of production images
# Keep last 5 versions of development images
# Keep last 3 versions of feature images
# Auto-delete images older than 30 days for features
```

### Security Scanning
```yaml
- name: Scan Images
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: ghcr.io/andreaendigital/carprice-backend:${{ steps.tags.outputs.tags }}
    format: 'sarif'
    output: 'trivy-results.sarif'
```

## Best Practices

1. **Semantic Versioning**: Use `v1.2.3` format for production releases
2. **Date Stamps**: Include date for tracking deployment history
3. **SHA References**: Always include commit SHA for traceability
4. **Environment Prefixes**: Clear distinction between prod/dev/staging
5. **Branch Naming**: Clean branch names for readable tags
6. **Immutable Tags**: Never overwrite existing version tags
7. **Security Labels**: Include metadata for compliance tracking
