
# RKTracker

Merging code from [KeypointTrackerCpp repo](https://github.com/Breakthrough/KeypointTrackerCpp) and existing local `cudaFSME` code (GPGPU accelerated not publically released yet).  Demonstration of existing GPGPU code (outlines what this repository will become):

[![Demonstration Video on Youtube](http://img.youtube.com/vi/_tEzrk0ISDk/0.jpg)](http://www.youtube.com/watch?v=_tEzrk0ISDk)

This is the repository for Keypoint Tracker FSME, a program which implements full-search motion estimation (FSME) to track user-selected keypoints in real-time.  A video file or camera/webcam stream can be opened and displayed, upon which you can click anywhere on the frame to add a keypoint at that location.  In subsequent frames, the keypoints will continually be tracked and update their location (motion estimation) using a fully exhaustive sum-and-difference search to find the best match/position.

RKTracker is written in C++ and requires OpenCV.  If you have a compatible GPU and the CUDA SDK, GPGPU acceleration can be enabled when compiling, allowing for a significant performance gain. 

--------

Licensed under BSD 2-Clause (see the LICENSE file for details).

Copyright (C) 2012-2016 Brandon Castellano.  All rights reserved.
