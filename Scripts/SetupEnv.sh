#!/bin/bash

echo "Changing directory to parent..."
cd ..

echo "Creating virtual environment..."

# Check if venv exists, if not, create one
if [ ! -d "env" ]; then
    python3 -m venv env
fi

echo "Activating virtual environment..."
source env/bin/activate

echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Environment setup complete. You can now activate it and start working."
