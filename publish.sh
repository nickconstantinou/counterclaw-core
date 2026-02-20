#!/bin/bash
# Publish CounterClaw to ClawHub
# Usage: ./publish.sh

set -e

VERSION="1.0.3"

echo "Publishing CounterClaw v$VERSION to ClawHub..."

# Ensure we're logged in
npx clawhub login --token "$CLAWHUB_TOKEN" --no-browser

# Publish with proper metadata
npx clawhub publish . \
    --version "$VERSION" \
    --env "TRUSTED_ADMIN_IDS" \
    --type "python-middleware" \
    --changelog "Fixed registry metadata mismatch, implemented Fail-Closed admin logic, sanitized documentation examples, added pathlib support for logging paths."

echo "✅ Published successfully!"
