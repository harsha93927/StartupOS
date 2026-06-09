# Building StartupOS Executable

To generate a Windows `.exe` file for StartupOS, follow these steps on your local machine:

## Prerequisites

- [Node.js](https://nodejs.org/) installed.
- [Python 3.x](https://www.python.org/) installed.

## Steps

1. **Install Dependencies**
   ```bash
   # In the root directory
   cd frontend && npm install
   cd ../electron && npm install
   cd ../backend && pip install -r requirements.txt
   ```

2. **Build the Frontend**
   ```bash
   cd frontend
   npm run build
   ```

3. **Build the Executable**
   ```bash
   cd electron
   npm run build
   ```

The portable Windows executable will be generated in the `electron/dist` folder.

## Running the Backend

StartupOS requires the FastAPI backend to be running.
```bash
cd backend
python -m uvicorn app.main:app --reload
```
