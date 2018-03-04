#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), November 29, 2014, at 08:30
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

def show_intro(win, escape_key_list):
    
    # Initialize components for Routine "start"
    startClock = core.Clock()
    
    text_2 = visual.TextStim(win=win, name='text_2',
                             text=u'Thank you for your participation in our subjective testing!\nYou will be watching a set of video sequences one after the other.\nWhile the video is playing, please record your quality of experience.\nAfter each video finishes, please record your overall quality of experience.\nIf you have any questions please ask them now.\n\nHit Enter to start!',
                             font=u'Arial',
                             pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0,
                             color=u'black', colorSpace='rgb', opacity=1,
                             depth=0.0);    
    
    if 0:
    
        mouse = event.Mouse(win=win)
    
        polygon = visual.Rect(
            win=win, name='polygon',
            width=(0.4, 0.4)[0], height=(0.4, 0.4)[1],
            ori=0, pos=(0, -.5),
            lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
            fillColor=[1,1,1], fillColorSpace='rgb',
            opacity=1, depth=-1.0, interpolate=True)

        continue_text = visual.TextStim(win=win, name='Continue',
            text='Continue',
            font='Arial',
            pos=(0, -.5), height=0.1, wrapWidth=None, ori=0,
            color='black', colorSpace='rgb', opacity=1,
            depth=-2.0)

                             
        while True:  # Forever.
            
            text_2.draw()
            polygon.draw()
            continue_text.draw()
            win.flip()

            if mouse.isPressedIn(polygon):
                continueRoutine = False
                break

    if 1:

        # ------Prepare to start Routine "start"-------
        t = 0
        startClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        #routineTimer.add(10.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        startComponents = [text_2]
        for thisComponent in startComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "start"-------
        while continueRoutine:# and routineTimer.getTime() > 0:
            # get current time
            t = startClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if t >= 0.0 and text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_2.tStart = t
                text_2.frameNStart = frameN  # exact frame index
                text_2.setAutoDraw(True)
            #frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            #if text_2.status == STARTED:# and t >= frameRemains:
                #text_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in startComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    #break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if event.getKeys(keyList=escape_key_list):
                print(1)#core.quit()
            if event.getKeys(keyList=["return"]):
                continueRoutine = False
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
                
        # -------Ending Routine "start"-------
        for thisComponent in startComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
def check_subject_info(expInfo, stored_scores_dir):
    
    valid_subject = 1
    subject_id = '-1'
    subject_session = '-1'
    
    if expInfo['Subject_id'] == '':
        print("Subject did not enter id, exiting.")
        valid_subject = 0
    else:
        subject_id = int(expInfo['Subject_id'])
        
    if expInfo['session'] == '':
        print("Subject did not enter session, exiting.")
        valid_subject = 0
    elif np.int(expInfo['session']) < 0 or np.int(expInfo['session']) > 2:
        print("Session # invalid, exiting.")
        valid_subject = 0
    else:
        subject_session = int(expInfo['session'])
    
    save_dest = stored_scores_dir + 'Subject_' + str(subject_id) + '_Session_' + str(subject_session)
    
    if os.path.isfile(save_dest + '.csv'):
        print("This session and subject id already exists.")
        valid_subject = 0
        
    return save_dest, valid_subject, subject_id, subject_session
   
def after_train_text(win, escape_key_list):
    
    after_train_screen = visual.TextStim(win=win, name='after_train_screen',
                         text=u'This ends your training. Hit Enter to proceed to testing!',
                         font=u'Arial',
                         pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0,
                         color=u'black', colorSpace='rgb', opacity=1,
                         depth=0.0);

    continueRoutine = True

    startComponents = [after_train_screen]
    for thisComponent in startComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    while continueRoutine:

        if after_train_screen.status == NOT_STARTED:
            after_train_screen.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True

        if event.getKeys(keyList=["return"]):
            continueRoutine = False

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "start"-------
    for thisComponent in startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
    return 1

def goodbye_screen(win, escape_key_list):
    
    endClock = core.Clock()
    
    text = visual.TextStim(win=win, name='text',
                       text=u'The test is now over.\nYou may now exit the room.\nThank you for your participation!',
                       font=u'Arial',
                       pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                       color=u'black', colorSpace='rgb', opacity=1,
                       depth=0.0);

    continueRoutine = True

    endComponents = [text]
    for thisComponent in endComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
            
    endClock.reset()

    tzero = endClock.getTime()

    while continueRoutine:

        t = endClock.getTime()

        if text.status == NOT_STARTED:

            text.setAutoDraw(True)

        if t > 5 + tzero:
           break

        if not continueRoutine:  # a component has requested a forced-end of Routine
            break

        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "end"-------
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
    return 1
    
def get_final_score(win, rating_final, escape_key_list):
 
    continueRoutine = True
    rating_final.reset()

    trialComponents = [rating_final]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
            
    while continueRoutine:
        
        rating_final.draw()    
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished  
                
        # check for quit (the Esc key)
        if event.getKeys(keyList=escape_key_list):
            core.quit()
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    final_score = rating_final.getRating()
    return final_score
            
def train_subject(win, train_videos, train_audios, rating_continuous, rating_final, escape_key_list):
    
    movie = visual.MovieStim3_christos(win=win, name='movie',units='pix', 
    filename=train_videos[0], noAudio=False, audio_filename=train_audios[0],
    ori=0, pos=[0, 0], opacity=1,
    size=[1920, 1080],
    depth=0.0,
    )

    for video_file, audio_file in zip(train_videos, train_audios):

        #------Prepare to start Routine "trial"-------
        t = 0

        # update component parameters for each repeat
        movie.setMovie(video_file, audio_file)

        rating_continuous.reset()

        # keep track of which components have finished
        trialComponents = [movie, rating_continuous]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        current_frame_time = []
        continuous_scores = []

        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine: #and routineTimer.getTime() > 0:
            
            # *movie* updates
            if t >= 0.0 and movie.status == NOT_STARTED:
		win.setColor([-1, -1, -1])
                # keep track of start time/frame for later
                movie.tStart = t  # underestimates by a little under one frame
                movie.play()
            elif movie.status == STARTED:# and t <= timeout:#(timeout-win.monitorFramePeriod*0.75): #most of one frame period left
                movie.draw()
                rating_continuous.draw()
            if movie.status == STARTED:
                continuous_scores.append(rating_continuous.getRating())
                current_frame_time.append(movie.getCurrentFrameTime())
            
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            if movie.status == FINISHED:
                continueRoutine = False
		win.setColor([0, 0, 0])
                
            # check for quit (the Esc key)
            if event.getKeys(keyList=escape_key_list):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        final_score = get_final_score(win, rating_final, escape_key_list)
                
                
                
