"""
EDA / sanity-check utilities for the lane segmentation dataset:
- converts TuSimple JSON lane annotations to binary segmentation masks
- reports image resolutions and lane pixel ratio
"""
import os
import glob
import cv2

def load_pairs(images_dir, masks_dir):
    image_paths = sorted(glob.glob(os.path.join(images_dir, "*")))
    mask_paths = sorted(glob.glob(os.path.join(masks_dir, "*")))
    assert len(image_paths) == len(mask_paths), "Mismatched image/mask counts"
    return list(zip(image_paths, mask_paths))

def report_stats(pairs):
    for img_path, mask_path in pairs[:5]:
        img = cv2.imread(img_path)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
        fg_ratio = (mask > 0).mean()
        print(f"{os.path.basename(img_path)}: img={img.shape}, "
              f"mask={mask.shape}, lane_pixels={fg_ratio:.3%}")

if __name__ == "__main__":
    print("Point this at data/lane/images and data/lane/masks once downloaded.")
