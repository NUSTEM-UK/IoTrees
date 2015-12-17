#!/usr/bin/python
#-----------------------------------------------------------------------
# Internet of Trees
# Run on a Raspberry Pi with Pimoroni Unicorn HAT; sets LED colour from 
# received Tweet data.
# 
# Based heavily on example code from Python Twitter Tools, http://mike.verdone.ca/twitter/
# Uses rgb_to_kelvin by petrklus, https://gist.github.com/petrklus/b1f427accdf7438606a6
# itself based on work by Tanner Helland, http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/
# Uses code based on Pimoroni Unicorn HAT examples,  https://github.com/pimoroni/unicorn-hat
# Extract hex strings example from http://stackoverflow.com/questions/18737788/extract-hexadecimal-number-from-string
#
# Author: Jonathan Sanderson, for Think Physics, Northumbria University
# Version: December 17th 2015
# 
#-----------------------------------------------------------------------

from kelvin_to_rgb import *
from hex_to_rgb import *
from twitter import *
import time
import re
import unicornhat as unicorn

unicorn.brightness(1.0)

def colour_change(value):
    for y in range(8):
        for x in range(8):
            unicorn.set_pixel(x,y,int(value[0]), int(value[1]), int(value[2]))
            unicorn.show()
            time.sleep(0.05)

# Username we're treating tweets to as input
username = "thinkphysicsne"

# sleep between tweets to avoid flooding.
sleep_time = 1

# load API credentials
config = {}
print("Loading config file\n")
execfile("config.py", config)

# Create Twitter API object
auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"])
twitter = Twitter(auth = auth)
stream = TwitterStream(domain = "userstream.twitter.com", auth = auth, secure = True)

# Iterate over tweets for this user stream
tweet_iter = stream.user()
for tweet in tweet_iter:
    # Does this tweet contain any parsed entities? If not, skip it.
    if "entities" not in tweet:
        continue
    
    # Extract user mentions
    mentions = tweet["entities"]["user_mentions"]
    mentioned_users = [ mention["screen_name"] for mention in mentions ]
	
    # Are any of those mentions for the watched user?
    if username in mentioned_users:
        # Output sender and tweet text
        print "\n ========================================= \n"
        print "Tweet from @%s" % tweet["user"]["screen_name"]
        print "Tweet text: %s" % tweet["text"]
        
        # Run hex extraction on text
        extract_hex = re.findall(r'#[0-9A-Fa-f]{6}', tweet["text"], re.I)
        print "Extracted hex codes: %s" % extract_hex
        
        # Run Kelvin extraction on text
        extract_kelvin = re.findall(r'[0-9]{4,6}[kK]', tweet["text"], re.I)
        print "Extracted Kelvin temperatures: %s" % extract_kelvin
        
        # Test if we have any Kelvin results, then clean up and convert to RGB:
        if len(extract_kelvin):
            extract_kelvin = ''.join(extract_kelvin[0]) # get the first Kelvin extraction, as a list
            extract_kelvin = extract_kelvin.rstrip('K') # strip trailing K, if any
            extract_kelvin = extract_kelvin.rstrip('k') # strip trailing k, if any
            extract_kelvin = extract_kelvin.rstrip(' ') # strip trailing space, if any
            extract_kelvin = int(''.join(extract_kelvin)) # convert to string then cast to integer
            kelvin_RGB = kelvin_to_rgb(extract_kelvin)
            print "Kelvin RGB target: %s" % (kelvin_RGB,)
            print "Execute Unicorn to Kelvin RGB target"
            colour_change(kelvin_RGB)
        
        # Kelvin input preferred (because Physics, obviously), but fall back to hex if that's present:
        elif len(extract_hex):
            # discard all but first match, convert to string before passing to hex_to_rgb
            hex_RGB = hex_to_rgb(''.join(extract_hex[0]))
            print "Hex RGB target: %s" % (hex_RGB,)
            print "Execute Unicorn to Hex RGB target"
            colour_change(hex_RGB)
	    
        # Remainder code from Twitter-Stream-Responder example, left as stub for auto-thanks if one should wish to implement that
        # status = "@%s thanks for the mention" % tweet["user"]["screen_name"]
        # try:
        #     twitter.statuses.update(status = status)
        # except Exception, e:
        #     print " - failed (maybe a duplicate?): %s" % e
        
    time.sleep(sleep_time)