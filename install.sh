#!/usr/bin/env bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to add directory to PATH
add_to_path() {
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        setx PATH "%PATH%;$1"
    else
        echo "export PATH=\$PATH:$1" >> ~/.bashrc
        source ~/.bashrc
    fi
}

# Check Python version
if ! command_exists python3.11; then
    echo "Error: Python 3.11 or higher is required."
    exit 1
fi

# Check if Poetry is installed
if ! command_exists poetry; then
    echo "Error: Poetry is required. Please install it first."
    exit 1
fi

# Install URS
echo "Installing URS..."
git clone --depth=1 https://github.com/JosephLai241/URS.git
cd URS
pip install numpy
poetry install
poetry run maturin develop --release

# Install your CLI tool
echo "Installing Manhwa Analyzer CLI..."
cd ..
git clone https://github.com/SpecialistSteak/manhwa-scraper-cli.git
cd manhwa_analyzer
poetry install

# Add your CLI to PATH
CLI_DIR=$(pwd)
add_to_path "$CLI_DIR"

echo "Installation complete!"
echo "Please restart your terminal or run 'source ~/.bashrc' (on Unix-like systems) to update your PATH."