import os
import subprocess
import sys

def install_python_dependencies():
    print("Installing Python dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "backend/requirements.txt"])

def install_node_dependencies():
    print("Installing Node.js dependencies for frontend and Electron...")
    subprocess.check_call(["npm", "install"], cwd="frontend")
    subprocess.check_call(["npm", "install"], cwd="electron")

def build_frontend():
    print("Building React frontend...")
    subprocess.check_call(["npm", "run", "build"], cwd="frontend")

def package_electron_app():
    print("Packaging Electron app...")
    subprocess.check_call(["npm", "run", "package-win"], cwd="electron")

def start_backend_server():
    print("Starting FastAPI backend server...")
    subprocess.check_call([sys.executable, "-m", "uvicorn", "backend.app:app", "--reload"])

def main():
    install_python_dependencies()
    install_node_dependencies()
    build_frontend()
    package_electron_app()
    print("Setup completed successfully!")

if __name__ == "__main__":
    main()