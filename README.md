# From-video-to-3D-object
From video file to a 3D object via NeRF  - the project is based on instant-ngp
<p float="center">
  <a >
    <img src="data/meta data/DroneAruco-gif.gif" width="350" />
  </a>
  <a >
    <img src="data/meta data/MeshLabres-gif.gif" width="350" />
  </a>
</p>

## Description:
This project will take you step by step to create a 3D object file from a video input.
The process can be divided into 4 main consecutive stages:
1. From video file to ordered indexed frames - OpenCV
2. From indexed frames into valid instant-ngp NeRF input (.json) - COLMAP 
  - A tool for visualization of the camera position based on the COLMAP output is provided
3. From indexed frames and COLMAP output into a NeRF-rendered scene - Instant-ngp by NVIDIA
4. From rendered scene into 3D (.STL or .obj) object - Instant-ngp and MeshLab


## Installation:
- First and foremost you need a GPU for this project that is compatible with [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit).
- Follow the download, installation and configuration of [Instant-NGP](https://github.com/NVlabs/instant-ngp).
- All system requirements should be aligned and based on the configuration of Instant-NGP as it is the most delicate part of the process.
- It is worth mentioning that the COLMAP part is built in the Instant-NGP project.
- Download [MeshLab](https://www.meshlab.net/) to simullate the result in a 3D environment.

### From video file to ordered indexed frames - OpenCV:
After downloading and installing the [Instant-NGP](https://github.com/NVlabs/instant-ngp) project, copy and paste the current project files into the Instant-NGP directory:
* [video_to_frames](video_to_frames.py)
* [video_to_COLMAP](video_to_COLMAP.py)
* [visualize_COLMAP_output](visualize_COLMAP_output.py)
  
To split the video file to frames - run video_to_frames.py
Notice - the video to frames is embedded in the video to COLMAP file in the next part.
### From indexed frames into valid instant-ngp NeRF input (.json) - COLMAP:
To create a valid NeRF input - i.e video to COLMAP run the script [video_to_COLMAP](video_to_COLMAP.py)
The process will run as follows:
1. You will be asked for the path to the source video file.
2. You will be given the current fps of the video the total number of frames, and be asked for the preferred frame sample rate per second - for example: 2 fps.
3. COLMAP will run automatically on the output frames and generate a transforms.json - the input for the NeRF program
4. You will be asked if you want to visualize the camera position as it perceived in the COLMAP output:
   <p float="center">
  <a >
    <img src="data/meta data/visualcam-gif.gif" width="350" />
  </a>
</p>

### From indexed frames and COLMAP output into a NeRF-rendered scene - Instant-ngp by NVIDIA:
Run  [Instant-NGP](https://github.com/NVlabs/instant-ngp) as described in the project, and make sure that the transforms.json is in the correct path (inside the data folder)
### From rendered scene into 3D (.STL) object - Instant-ngp and MeshLab:
To extract a 3D object from the rendered scene - follow [Export 3D Object from Nvidia (instant-ngp) NeRF and load it into Blender and MeshLab](https://www.youtube.com/watch?v=55XKtYOIB7Y)
This video demonstrates how to use the Instant-NGP built-in API to produce a 3D object from the scene.


### Results:
The 3D object [example](data/Results/base/base.obj) - an .obj file that can be upload and open in MeshLab
<p float="center">
  <a >
    <img src="data/meta data/NeRFenv-gif.gif" width="350" />
  </a>
  <a >
    <img src="data/meta data/MeshLabres-gif.gif" width="350" />
  </a>
</p>

