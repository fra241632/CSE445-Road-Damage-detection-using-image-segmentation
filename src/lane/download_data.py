"""
Download and organize the TuSimple lane segmentation dataset.
Usage: python src/lane/download_data.py
"""
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "lane")

def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    print("Place TuSimple archives (see data/README.md) into:", DATA_DIR)
    print("Then run src/lane/preprocess.py to convert lane annotations to binary masks.")

if __name__ == "__main__":
    main()
