# scripts/download_data.py

import tarfile
import os
import shutil

def extract_tar_gz(filepath, extract_to):
    print(f"Extracting {filepath} to {extract_to} ...")
    with tarfile.open(filepath, "r:gz") as tar:
        tar.extractall(path=extract_to)
    print("Extraction complete.\n")

def move_lab_files(source_dir, dest_dir):
    print("Moving .lab files...")
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".lab"):
                full_src = os.path.join(root, file)
                shutil.move(full_src, os.path.join(dest_dir, file))
    print("Moved all .lab files.\n")

def move_chroma_files(source_dir, dest_dir):
    print("Moving chroma feature folders...")
    for subdir in os.listdir(source_dir):
        full_subdir = os.path.join(source_dir, subdir)
        if os.path.isdir(full_subdir):
            shutil.move(full_subdir, os.path.join(dest_dir, subdir))
    print("Moved chroma feature data.\n")

if __name__ == "__main__":
    print("🎶 Billboard Dataset Organizer 🎶")

    lab_tar = input("Enter path to billboard-2.0.1-lab.tar.gz: ").strip()
    chroma_tar = input("Enter path to billboard-2.0-chordino.tar.gz: ").strip()
    index_csv = input("Enter path to billboard-2.0-index.csv: ").strip()

    # Create temp folders to extract into
    tmp_lab = "data/tmp_labs"
    tmp_chroma = "data/tmp_chroma"
    os.makedirs(tmp_lab, exist_ok=True)
    os.makedirs(tmp_chroma, exist_ok=True)

    # Extract files
    extract_tar_gz(lab_tar, tmp_lab)
    extract_tar_gz(chroma_tar, tmp_chroma)

    # Move files to final destination
    move_lab_files(tmp_lab, "data/raw/lab_files")
    move_chroma_files(tmp_chroma, "data/raw/chroma_features")

    # Move index file
    shutil.copy(index_csv, "data/raw/index.csv")
    print("Copied index.csv")

    # Clean up temp dirs
    shutil.rmtree(tmp_lab)
    shutil.rmtree(tmp_chroma)

    print("\n✅ Dataset setup complete! 🎉")
