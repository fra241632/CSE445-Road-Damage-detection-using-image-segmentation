"""
Download and organize the crack detection dataset (CRACK500 / DeepCrack).
Usage: python src/crack/download_data.py
"""
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "crack")

def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    print("Place CRACK500 / DeepCrack archives (see data/README.md) into:", DATA_DIR)
    print("Then run src/crack/preprocess.py to organize image/mask pairs.")

if __name__ == "__main__":
    main()
