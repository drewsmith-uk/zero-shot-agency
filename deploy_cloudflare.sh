#!/bin/bash
# Fallback Direct Deployment Script for Cloudflare Pages
# Bypasses GitHub auth and mobile browser loop by deploying directly via Wrangler CLI

set -e

echo "Deploying static site to Cloudflare Pages..."

# Navigate to the mkdocs repository
cd /home/claw/workspace/zero-shot-agency

# Build the MkDocs site
echo "Building site with MkDocs..."
if [ -d "venv" ]; then
    source venv/bin/activate
fi
mkdocs build

# Deploy directly via Wrangler
echo "Deploying to Cloudflare Pages via Wrangler..."
npx wrangler pages deploy site/ --project-name=geo-wiki

echo "✅ Direct deployment complete!"
