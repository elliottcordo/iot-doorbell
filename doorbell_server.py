#!/usr/bin/python
from sseclient import SSEClient
import json
import pygame
import os


accessToken = 'xxx'
# sparkURL = 'https://api.spark.io/v1/devices/' + deviceID + '/events/cat/?access_token=' + accessToken
sound_directory = '/Users/elliottcordo/Projects/Scratch/photon'
bell_filename = 'uptown-funk---bruno-mars.wav'

def parse_msg (msg):
    try:
        output = msg.data
        if type(output) is not str:
            json_out = json.loads(output)
            return json_out['data']
    except:
        pass

pygame.mixer.init(44100, -16, 2, 2048)

def load_sound(sound_filename, directory):
    """load the sound file from the given directory"""
    fullname = os.path.join(directory, sound_filename)
    sound = pygame.mixer.Sound(fullname)
    return sound

sparkURL = 'https://api.particle.io/v1/devices/events/doorbell/?access_token=' + accessToken
messages = SSEClient(sparkURL)

doorbell = load_sound(bell_filename, sound_directory)

for msg in messages:
    if msg:
        status = parse_msg(msg)
        if status == 'pressed':
            doorbell.play()


        # pprint.pprint(data)




