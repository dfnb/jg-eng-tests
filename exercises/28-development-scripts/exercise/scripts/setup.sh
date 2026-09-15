#!/usr/bin/env bash
mkdir -p .local-state
echo applied >> .local-state/migrations.log
cp fixtures/sample.json .local-state/data.json
echo ready
