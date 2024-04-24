import subprocess
from video_to_frames import extract_frames
from visualize_COLMAP_output import plot_camera_positions_with_direction
import shutil
import os


if __name__ == "__main__":
    # Option 1: Regular drone video
    video_path = input("Insert path to the video file, including the file itself.\n Enter here: ")

    # Get the directory of the current script
    # Define the project root directory
    # PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    # frames_save_path = os.path.join(PROJECT_ROOT, "\instant-ngp\data\\v2obj\\frames")
    # frames_save_path = PROJECT_ROOT + r"\instant-ngp\data\v2obj\frames"

    frames_save_path = r".\instant-ngp\data\v2obj\frames"
    if not os.path.exists(frames_save_path):
        os.makedirs(frames_save_path)

    # step 1 - from MP4 input, make set of images
    number_of_samples = extract_frames(video_path, frames_save_path)
    print("{} samples created".format(number_of_samples))

    '''
    from the set of frames, run COLMAP and process the data to input it to the NERF network
    There is a problem with the images source path input - can be located in the wider project directory.
    Only under the instant-ngp directory under data directory.
    '''
    images_path = frames_save_path

    # Set the path to the colmap2nerf.py script
    # colmap2nerf_script_path = PROJECT_ROOT + r'.\instant-ngp\scripts\colmap2nerf.py'
    colmap2nerf_script_path =  r'.\instant-ngp\scripts\colmap2nerf.py'

    # Set the arguments for colmap2nerf.py
    colmap2nerf_arguments = [
        '--colmap_matcher', 'exhaustive',
        '--run_colmap',
        '--aabb_scale', '32',
        '--images', images_path
    ]

    # Construct the command-line arguments
    command = [
                  'python',
                  colmap2nerf_script_path
              ] + colmap2nerf_arguments

    # Execute the command using subprocess
    subprocess.run(command)

    # subprocess.run(['python', './scripts/colmap2nerf.py --colmap_matcher exhaustive --run_colmap --aabb_scale 32'])
    # subprocess.run(['python', 'colmap2nerf.py --colmap_matcher exhaustive --run_colmap --aabb_scale 32'])

    visualization_flag = input("Do you want to visualize the camera position from COLMAP? (y/n): ")
    visualization_flag = True if visualization_flag == 'y' or visualization_flag == 'Y' else False



    if visualization_flag:
        with open('transforms.json', 'r') as file:
            json_data = file.read()
        plot_camera_positions_with_direction(json_data)
        # except FileNotFoundError:
        #     print("File 'transforms.json' not found. Proceeding without it.")

    transforms_file = 'transforms.json'
    destination_dir = r'\instant-ngp\data\v2obj'

    # Check if the source file exists
    if os.path.exists(transforms_file):
        # Create the destination directory if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Move the file to the destination directory
        shutil.move(transforms_file, destination_dir)




