#!/bin/#!/usr/bin/env bash

echo "Hello World"

. venv/bin/activate

export FLASK_CONFIG=development
export FLASK_APP=run.py
# python run.py
echo "added flask config and activate venv"
