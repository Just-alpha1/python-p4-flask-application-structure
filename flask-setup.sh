#!/bin/bash
# Flask Development Environment Setup Script

# This script should be sourced in your pipenv shell
# Usage: source flask-setup.sh

echo "🚀 Starting Flask Development Environment..."

# Check if we're in the right directory
if [ ! -f "server/app.py" ]; then
    echo "❌ Error: server/app.py not found. Please run from project root directory."
    return 1
fi

# Start Flask in background
echo "🔥 Starting Flask server on http://127.0.0.1:5555"
cd server && python app.py &
FLASK_PID=$!
cd ..

echo "✅ Flask started with PID: $FLASK_PID"
echo "🌐 Your Flask app is running on http://127.0.0.1:5555"
echo "💡 Your routes:"
echo "   - Main page: http://127.0.0.1:5555"
echo "   - User profiles: http://127.0.0.1:5555/username"
echo ""
echo "💡 Flask will auto-restart when you modify server/app.py"
echo "💡 Type 'exit' to stop Flask and exit the shell"
echo ""

# Function to cleanup Flask when shell exits
cleanup_flask() {
    echo ""
    echo "🛑 Stopping Flask server (PID: $FLASK_PID)..."
    kill $FLASK_PID 2>/dev/null
    wait $FLASK_PID 2>/dev/null
    echo "👋 Development environment stopped!"
}

# Set trap to cleanup on shell exit
trap cleanup_flask EXIT

# Export variables for convenience
export FLASK_APP=server/app.py
export FLASK_ENV=development
export FLASK_RUN_PORT=5555
