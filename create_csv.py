import os
import csv
from pathlib import Path


def create_image_paths_csv(root_dir: str, output_csv: str):
    """
    Creates a CSV file containing image paths from a directory with subfolders.

    Args:
        root_dir (str): The path to the root directory containing subfolders with images.
        output_csv (str): The path to save the output CSV file.
    """

    image_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
                image_path = str(Path(dirpath) / filename)
                image_paths.append({"image_path": image_path})

    with open(output_csv, "w", newline="") as csvfile:
        fieldnames = ["image_path"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(image_paths)

    print(f"CSV file created at: {output_csv}")


if __name__ == "__main__":
    root_directory = "some_images"  # Replace with your root dir
    output_file = "image_paths.csv"  # Name of output CSV file

    create_image_paths_csv(root_directory, output_file)
