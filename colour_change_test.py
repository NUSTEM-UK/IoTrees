from kelvin_to_rgb import *
from hex_to_rgb import *
import time
import re
import unicornhat as unicorn

unicorn.brightness(1.0)

def colour_change(red,green,blue):
    for y in range(8):
        for x in range(8):
            unicorn.set_pixel(x,y,red,green,blue)
            unicorn.show()
            time.sleep(0.05)

testString1 = "This is a test #ffffff"
testString2 = "This is another test 3500 k"
testString3 = "This is a third test #aaaaaa 15000K"
testString4 = "This is a fourth test #8a9a2 #8a9a2a"

# Run hex greps
result1 = re.findall(r'#[0-9A-Fa-f]{6}', testString1, re.I)
result2 = re.findall(r'#[0-9A-Fa-f]{6}', testString2, re.I)
result3 = re.findall(r'#[0-9A-Fa-f]{6}', testString3, re.I)
result4 = re.findall(r'#[0-9A-Fa-f]{6}', testString4, re.I)

print "result 1: %s" % result1
print "result 2: %s" % result2
print "result 3: %s" % result3
print "result 4: %s" % result4

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

# Need to cast to string before passing to hex_to_rgb.
if len(result1):
    result1 = hex_to_rgb(''.join(result1[0])) #discard all but first element
    print "result 1 RGB: %s" % (result1,) #singleton of tuple, so it prints. Ugh.
    red = result1[0]
    print red
    green = result1[1]
    print green
    blue = result1[2]
    print blue
    colour_change(red,green,blue)


if len(result2):
    result2 = hex_to_rgb(''.join(result2[0]))
    print "result 2 RGB: %s" % (result2,)
    colour_change(result2,)

if len(result3):
    result3 = hex_to_rgb(''.join(result3[0]))
    print "result 3 RGB: %s" % (result3,)
    colour_change(result3,)

# Next test fails, because two returned hex values.
if len(result4):
    result4 = hex_to_rgb(''.join(result4[0]))
    print "result 4 RGB: %s" % (result4,)
    colour_change(result4,)

