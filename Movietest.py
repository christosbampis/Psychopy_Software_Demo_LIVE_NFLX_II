#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), November 29, 2014, at 08:30
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0

from psychopy import prefs
prefs.general['audioLib'] = ['pygame']

from psychopy import visual, core, data, event, logging, gui, sound

from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray, unique
from numpy.random import random, randint, normal, shuffle
import pickle
import os  # handy system and path functions

from test_misc_utils import show_intro, check_subject_info, after_train_text, goodbye_screen, get_final_score, train_subject

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Movietest'
expInfo = {'Subject_id':'', 'session':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

stored_scores_dir = _thisDir + os.sep + 'data/'
save_dest = -1
save_dest, valid_subject, subject_id, session = check_subject_info(expInfo, stored_scores_dir)

if not valid_subject:
    core.quit()

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=save_dest)
#save a log file for detail verbose info
logFile = logging.LogFile(save_dest+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
#escape_key_list = ["escape"]
escape_key_list = []

# Setup the Window
win = visual.Window(size = (1920, 1080), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=False,
    )

#win_not_gray = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
#    monitor='testMonitor', color=[-1, -1, -1], colorSpace='rgb',
#    blendMode='avg', useFBO=True,
#    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess
    
rating_continuous = visual.RatingScale(win=win, name='rating', precision = '100', marker=u'slider', textColor = 'black', markerStart=50,
    showValue = False, tickHeight = 0.0, size=1.5, pos=[0.0, -0.92], labels=[''], scale='', low=1, high=100, stretch = 0.75, mouseOnly=True,
    markerColor='Gray')
rating_final = visual.RatingScale(win=win, name='rating', precision = '100', marker=u'slider', textColor = 'black', showValue = False, minTime=0.01,
    tickHeight = 0.0, size=1.0, pos=[0.0, -0.0], low=1, high=100, labels=[u'Bad', u' Excellent'], mouseOnly=True,
    scale=u'Please rate your overall quality of experience.')

rating_continuous_train = visual.RatingScale(win=win, name='rating', precision = '100', marker=u'slider', textColor = 'black', markerStart=50,
    showValue = False, tickHeight = 0.0, size=1.5, pos=[0.0, -0.92], labels=[''], scale='', low=1, high=100, stretch = 0.75, mouseOnly=True,
    markerColor='Gray')
rating_final_train = visual.RatingScale(win=win, name='rating', precision = '100', marker=u'slider', textColor = 'black', showValue = False, minTime=0.01,
    tickHeight = 0.0, size=1.0, pos=[0.0, -0.0], low=1, high=100,labels=[u'Bad', u' Excellent'], mouseOnly=True,
    scale=u'Please rate your overall quality of experience.')

main_dir = '/media/christos/Subjective_Study/LIVE_NFLX_Plus_Sources/'

playlist_dir = main_dir + 'Playlists/'
video_dir = main_dir + 'assets_mp4/'
audio_dir = main_dir + 'assets_mp4/Audio/'
train_dir = main_dir + 'TrainingVideos/'

video_train_files = [train_dir + 'train_1.mp4', train_dir + 'train_2.mp4', train_dir + 'train_3.mp4']
audio_train_files = [train_dir + 'train_1_44100.wav', train_dir + 'train_2_44100.wav', train_dir + 'train_3_44100.wav']

playlist_file = playlist_dir + 'Subject_' + str(subject_id) + '_session_' + str(session) + '.txt'

with open(playlist_file, 'r') as f:
    multimedia_files = f.readlines()

# load the video and audio files separately, by changing the movie3.py
video_files = []
audio_files = []
for multimedia_file in multimedia_files:
    
    video_file = multimedia_file.split(" ")[0]
    audio_file = multimedia_file.split(" ")[1].split("\n")[0]

    video_files.append(video_dir + video_file)
    audio_files.append(audio_dir + audio_file)

show_intro(win, escape_key_list)

run_those = 0
run_those_2 = 0

need_training = True
if session > 0:
    need_training = False

if need_training:
    train_subject(win, video_train_files, audio_train_files, rating_continuous_train, rating_final_train, escape_key_list)
    after_train_text(win, escape_key_list)

do_test = True

if do_test:
    
    # Initialize components for Routine "trial"
    trialClock = core.Clock()
        
    movie = visual.MovieStim3_changed(win=win, name='movie',units='pix',
        filename=video_files[0], noAudio=False, audio_filename=audio_files[0],
        ori=0, pos=[0, 0], opacity=1,
        size=[1920, 1080],
        depth=0.0,
        )

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started

    for video_file, audio_file in zip(video_files, audio_files):

        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1

        # update component parameters for each repeat
        movie.setMovie(video_file, audio_file)

        rating_continuous.reset()

        # keep track of which components have finished
        trialComponents = [movie, rating_continuous]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        current_frame_time = []
        current_frame_time_many = []
        continuous_scores = []

        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine: #and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *movie* updates
            if t >= 0.0 and movie.status == NOT_STARTED:
                # keep track of start time/frame for later
		win.setColor([-1, -1, -1])
                movie.tStart = t  # underestimates by a little under one frame
                movie.frameNStart = frameN  # exact frame index
                movie.play()
            elif movie.status == STARTED:# and t <= timeout:#(timeout-win.monitorFramePeriod*0.75): #most of one frame period left
                movie.draw()
            if t > 0 and movie.status != FINISHED:
                rating_continuous.draw()
                #if movie.status != FINISHED:
                run_those += 1
                continuous_scores.append(rating_continuous.getRating())
                current_frame_time.append(movie.getCurrentFrameTime())
            
            run_those_2 += 1
            current_frame_time_many.append(movie.getCurrentFrameTime())
                
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            if movie.status == FINISHED:
                continueRoutine = False
                movie_audioStream = None
                win.setColor([0, 0, 0])

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=escape_key_list):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                
        final_score = get_final_score(win, rating_final, escape_key_list)

        Nrendered = len(current_frame_time)
        Nframes = len(unique(current_frame_time))
        Nframes_many = len(unique(current_frame_time_many))
        Nscores = len(continuous_scores)

        # store data for thisExp (ExperimentHandler)
        thisExp.addData('subject_id', subject_id)
        thisExp.addData('video', video_file)
        thisExp.addData('session', session)
        thisExp.addData('Nrendered', Nrendered)
        thisExp.addData('Nframes', Nframes)
        thisExp.addData('Nscores', Nscores)
        thisExp.addData('final_score', final_score)
        thisExp.addData('continuous_scores', continuous_scores)
        
        thisExp.nextEntry()

    goodbye_screen(win, escape_key_list)

win.close()
core.quit()
