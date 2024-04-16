# From-video-to-3D-object
From video file to a 3D object via NeRF  - the project is based on instant-ngp

## Description:
This project will take you step by step to create a 3D object file from a video input.
The process can be divided into 4 main consecutive stages:
1. From video file to ordered indexed frames - OpenCV
2. From indexed frames into valid instant-ngp NeRF input (.json) - COLMAP 
3. From indexed frames and COLMAP output into a NeRF-rendered scene - Instant-ngp by NVIDIA
4. From rendered scene into 3D (.STL) object - Instant-ngp and MeshLab

## Installation:
- First and foremost you need a GPU for this project that is compatible with [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit).
- Follow the download and installation and configuration of [Instant-NGP](https://github.com/NVlabs/instant-ngp).
- All system requirements should be aligned and based on the configuration of Instant-NGP as it is the most delicate part of the process.
- It is worth mentioning that the COLMAP part is built in the Instant-NGP project.
- Download [MeshLab](https://www.meshlab.net/) to simullate the result in a 3D environment.

