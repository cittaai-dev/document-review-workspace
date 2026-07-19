#!/usr/bin/env bash
set -e
pip install -r requirements.txt
python -m app.seed
uvicorn app.main:app --reload
