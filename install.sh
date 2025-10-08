#!/bin/bash

# Spanish Distant Reader - Installation Script
# Installs required dependencies and sets up the tool

echo "🎼 Spanish Distant Reader - Installation"
echo "========================================"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "   Please install Python 3 from https://python.org"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is required but not installed."
    echo "   Please install pip3"
    exit 1
fi

echo "✅ pip3 found"

# Install required packages
echo "📦 Installing required Python packages..."

pip3 install matplotlib wordcloud --user

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
else
    echo "⚠️  Some dependencies may not have installed correctly."
    echo "   You can try installing manually with:"
    echo "   pip3 install matplotlib wordcloud"
fi

# Make script executable
chmod +x spanish-distant-reader.py

echo ""
echo "🎉 Installation complete!"
echo ""
echo "📋 Usage:"
echo "   python3 spanish-distant-reader.py <carrel-name> <source-directory>"
echo ""
echo "📖 Example:"
echo "   python3 spanish-distant-reader.py mi-corpus ./archivos-txt/"
echo ""
echo "📚 For more information, see README.md"
echo ""