# Network Speed Test and Optimization Tool

## Description

This project is a desktop application that allows users to test their network speed, receive AI-based suggestions for optimization, and apply network optimizations. The application is built with React for the frontend, FastAPI (Python) for the backend, and Electron for packaging it as a Windows executable.

## Project Structure

```
network-speed-tool/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
│   └── __init__.py
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── components/
│   │   │   ├── SpeedTest.js
│   │   │   ├── AIAnalysis.js
│   │   │   └── Optimizations.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── App.css
│   ├── package.json
│   ├── package-lock.json
│   └── README.md
│
├── electron/
│   ├── main.js
│   ├── preload.js
│   ├── package.json
│   ├── package-lock.json
│   └── README.md
│
├── dist/
│   ├── network-speed-tool.exe
│
└── setup.py
```

## Installation

### Backend

1. Navigate to the `backend` directory:
   ```sh
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:
   ```sh
   uvicorn app:app --reload
   ```

### Frontend

1. Navigate to the `frontend` directory:
   ```sh
   cd frontend
   ```

2. Install the required packages:
   ```sh
   npm install
   ```

3. Start the React development server:
   ```sh
   npm start
   ```

### Electron

1. Navigate to the `electron` directory:
   ```sh
   cd electron
   ```

2. Install the required packages:
   ```sh
   npm install
   ```

3. Start the Electron application:
   ```sh
   npm start
   ```

### Packaging

1. Navigate to the `electron` directory:
   ```sh
   cd electron
   ```

2. Run the packaging script:
   ```sh
   npm run package-win
   ```

## Usage

1. Start the FastAPI server.
2. Start the React development server.
3. Start the Electron application.
4. Use the application to test network speed, get AI suggestions, and apply network optimizations.

## License

This project is licensed under the MIT License.