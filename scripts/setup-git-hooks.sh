#!/bin/bash
# Setup Git hooks for the project

echo "Setting up Git hooks..."

# Copy pre-commit hook to .git/hooks
if [ -d ".git/hooks" ]; then
    cp .git-hooks/pre-commit .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    echo "✅ Pre-commit hook installed successfully!"
else
    echo "❌ .git directory not found. Are you in a Git repository?"
    exit 1
fi

echo ""
echo "Git hooks are now active. Templates will be built automatically before each commit."
