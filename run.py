import subprocess
import sys
import os

def main():
    """
    Launch the Streamlit app.
    """
    app_path = os.path.join("app", "app.py")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", app_path])
    except Exception as e:
        print(f"Error launching Streamlit app: {e}")

if __name__ == "__main__":
    main()
