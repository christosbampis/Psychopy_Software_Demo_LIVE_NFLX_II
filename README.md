=================================================================

-----------COPYRIGHT NOTICE STARTS WITH THIS LINE------------

Copyright (c) 2018 The University of Texas at Austin

All rights reserved. Permission is hereby granted, without written agreement and without license or royalty fees, to use, copy, modify, and distribute this code (the source files) and its documentation for any purpose, provided that the copyright notice in its entirety appear in all copies of this code, and the original source of this code, Laboratory for Image and Video Engineering (LIVE, http://live.ece.utexas.edu) and Center for Perceptual Systems (CPS, http://www.cps.utexas.edu) at the University of Texas at Austin (UT Austin, http://www.utexas.edu), is acknowledged in any publication that reports research using this code. The research is to be cited in the bibliography as:

Christos G. Bampis, Zhi Li, Ioannis Katsavounidis, Te-Yuan Huang, Chaitanya Ekanadham and Alan C. Bovik, Towards Perceptually Optimized End-to-end Adaptive Video Streaming, submitted to IEEE Transactions on Image Processing.

IN NO EVENT SHALL THE UNIVERSITY OF TEXAS AT AUSTIN BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF THIS DATABASE AND ITS DOCUMENTATION, EVEN IF THE UNIVERSITY OF TEXAS AT AUSTIN HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. THE UNIVERSITY OF TEXAS AT AUSTIN SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE DATABASE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, AND THE UNIVERSITY OF TEXAS AT AUSTIN HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.

-----------COPYRIGHT NOTICE ENDS WITH THIS LINE------------%

Author : Christos Bampis

The author is with the Laboratory for Image and Video Engineering (LIVE), Department of Electrical and Computer Engineering, The University of Texas at Austin, Austin, TX.

Kindly report any suggestions or corrections to cbampis@gmail.com.

=================================================================

This is a demo software implementation for the Psychopy-based subjective interface used in the LIVE-NFLX-II experiment. To use the code please first clone the latest Psychopy version from the repository and add movie3_changed.py in Psychopy/psychopy/psychopy/visual/ so that you are able to load the video and audio files separately, otherwise Psychopy was leading to a small audio glitch in the end of each video file.

The interface will allow you to extract continuous-time (per-frame) scores.
