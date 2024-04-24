import cv2 as cv
import os
import matplotlib.pyplot as plt

def extract_frames(input_video, output_directory):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Open the video file
    video_capture = cv.VideoCapture(input_video)

    # Get video properties
    frame_rate = video_capture.get(cv.CAP_PROP_FPS)
    total_frames = int(video_capture.get(cv.CAP_PROP_FRAME_COUNT))
    frames_per_second = 0
    while(frames_per_second < 1 or frames_per_second > round(frame_rate)-1 ):
        print("The video frame rate in fps is: {} and the total number of frames if the video is: {}".format(round(frame_rate),total_frames))
        frames_per_second = input("type the sample rate you wish to save. i.e the number of frame to save per second. From 1 to the current frame rate: ")
        frames_per_second = int(frames_per_second)
    # Calculate frame interval for desired frames per second

    frame_interval = int(frame_rate / frames_per_second)

    # Read and save frames
    frame_count = 0
    fames_saved = 0
    while True:
        success, frame = video_capture.read()

        if not success:
            break

        # Save frame every frame_interval frames
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_directory, f"frame_{frame_count // frame_interval}.jpg")

            # Display the image with the number added
            # plt.imshow(frame)
            # plt.show()
            fames_saved+=1
            cv.imwrite(frame_filename, frame)

        frame_count += 1
    return fames_saved

    # Release the video capture object
    video_capture.release()

