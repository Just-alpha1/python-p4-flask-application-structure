
# Flask Auto-Start Setup

## Quick Start - NEW SIMPLE WAY

**Instead of:** `pipenv install && pipenv shell`

**Use this:** `./flask-start`

This will automatically:
1. ✅ Install dependencies if needed
2. ✅ Start Flask on http://127.0.0.1:5555  
3. ✅ Open pipenv shell with Flask running in background
4. ✅ Stop Flask when you exit the shell

## Simple Usage

```bash
./flask-start
```

That's it! Flask will automatically start and your pipenv shell will be activated.

## Alternative Options

```bash
# Use the comprehensive development manager
./flask-dev run           # Flask + shell (recommended alternative)

# Or use the shell manually
./flask-dev shell         # Shell only
source flask-setup.sh     # Then start Flask manually

# Direct Flask commands
./flask-dev start         # Start Flask only
./flask-dev stop          # Stop Flask
```

## What Happens When You Use `./flask-start`

1. **Auto Dependencies**: Installs if Pipfile is newer than Pipfile.lock
2. **Flask Startup**: Starts Flask server on port 5555 in background  
3. **Shell Access**: Opens pipenv shell with Flask already running
4. **Auto-Cleanup**: Flask automatically stops when you exit the shell

## Access Your App

- **Main page**: http://127.0.0.1:5555
- **User profiles**: http://127.0.0.1:5555/username

## Exit Development

```bash
exit  # or Ctrl+D
```

Flask will automatically stop when you exit the shell.

## Workflow Comparison

**Before:**
```bash
pipenv install && pipenv shell
# Then manually: python server/app.py
```

**After (recommended):**
```bash
./flask-start
```

**Result:** Same pipenv access + automatic Flask startup! 🚀
