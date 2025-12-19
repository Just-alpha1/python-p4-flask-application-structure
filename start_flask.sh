

#!/bin/bash
# Flask Development Environment Launcher

echo "🚀 Starting Flask Development Environment..."

# Install dependencies if needed
if [ ! -f "Pipfile.lock" ] || [ "Pipfile" -nt "Pipfile.lock" ]; then
    echo "📦 Installing dependencies..."
    pipenv install
fi

# Start Flask in background
echo "🔥 Starting Flask server..."
python server/app.py &
FLASK_PID=$!

echo "✅ Flask started with PID: $FLASK_PID"
echo "🌐 Flask server is running on http://127.0.0.1:5555"
echo ""
echo "💡 Now activating pipenv shell..."

# Function to cleanup Flask when shell exits
cleanup() {
    echo ""
    echo "🛑 Shutting down Flask server..."
    kill $FLASK_PID 2>/dev/null
    echo "👋 Goodbye!"
}

# Set trap to cleanup on shell exit
trap cleanup EXIT

# Activate pipenv shell
exec pipenv shell
