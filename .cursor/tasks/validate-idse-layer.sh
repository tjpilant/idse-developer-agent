#!/usr/bin/env bash
echo "🔍 Validating IDSE Governance Layer..."
if [ ! -f ".idse-layer" ]; then
  echo "❌ Missing .idse-layer boundary marker!"
  exit 1
fi

if grep -R "GOVERNANCE LAYER NOTICE" idse-governance/ >/dev/null; then
  echo "✅ Governance layer notice found"
else
  echo "❌ Missing governance layer notices"
  exit 1
fi

echo "✅ IDSE Governance Layer validation passed!"
