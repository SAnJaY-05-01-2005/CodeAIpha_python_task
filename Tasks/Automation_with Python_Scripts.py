import os
import shutil

def organize_images():
    # 1. SETUP: Define directory paths
    # os.getcwd() gets the current working directory where this script is running
    source_folder = os.getcwd()
    
    # Define the name of the new folder where images will go
    # os.path.join is safer than manual string concatenation (works on Win/Mac/Linux)
    destination_folder = os.path.join(source_folder, "Images_Backup")

    # 2. CREATE FOLDER: Check if it exists; if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created new folder: {destination_folder}")
    else:
        print(f"Folder already exists: {destination_folder}")

    # 3. SCAN & MOVE: Loop through files in the source folder
    files_moved_count = 0
    
    print(f"Scanning folder: {source_folder}...")

    # os.listdir() gives a list of all filenames in the directory
    for filename in os.listdir(source_folder):
        
        # Check if the file is a JPG (case-insensitive so .JPG and .jpg work)
        # We also want to make sure we don't try to move the folder itself!
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            
            # Construct full file paths
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            try:
                # shutil.move() does the actual moving of the file
                shutil.move(source_path, destination_path)
                print(f"Moved: {filename}")
                files_moved_count += 1
                
            except Exception as e:
                print(f"Error moving {filename}: {e}")

    # 4. SUMMARY
    print("-" * 30)
    if files_moved_count > 0:
        print(f"Success! Moved {files_moved_count} images to 'Images_Backup'.")
    else:
        print("No .jpg files found to move.")

# Run the automation
if __name__ == "__main__":
    # OPTIONAL: Create dummy files to test immediately if you have none
    # open("test1.jpg", "w").close() 
    # open("test2.jpg", "w").close()
    
    organize_images()