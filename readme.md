# Internet of Trees

Whatever the 'Next Big Thing' is, there's apparently going to be an Internet Of them. We think at least some of the Things should be trees -- Christmas trees. With sparkly lights.

This code drives coloured lights from a Twitter stream. It's a ghastly hack, but in initial testing it mostly works. It's also our first Python code, so, you know, be gentle.

## Project Story

You can [read up on the project in detail at the Think Physics website](http://thinkphysics.org/activity/internet-of-trees/ "Internet of Trees | ThinkPhysics"). The following is more of a developers/hackers guide for anyone wishing to replicate the tree, or something like it.

## Hardware

To replicate Think Physics' IoTree, you'll need:

1. A tree. We built [this design](http://www.instructables.com/id/Makedo-Christmas-tree/ "Makedo Cardboard Christmas tree: 2015 UPDATE") from Makedo on Instructables. Makedo is a terrific cardboard construction system with which you can quickly lash together big structures. We love it.
2. A [Raspberry Pi](https://www.raspberrypi.org). We used a Pi2 backed onto a [Pi touchscreen](https://www.raspberrypi.org/products/raspberry-pi-touch-display/), in a [Pimoroni stand](https://shop.pimoroni.com/products/raspberry-pi-7-touchscreen-display-with-frame), which all fitted neatly into the side of the Makedo Tree base. The Pi needs to be on a network; we used a [WiFi dongle](https://shop.pimoroni.com/products/official-raspberry-pi-wifi-dongle), since plugging things into our university network is frowned upon.
3. A [Pimoroni Unicorn HAT](https://shop.pimoroni.com/products/unicorn-hat), which is a nifty 8x8 array of individually-addressable RGB LEDs.

## Software

Requires:

* Unicorn HAT Python bindings: `\curl -sS get.pimoroni.com/unicornhat | bash`, if you're trusting; see [here](https://github.com/pimoroni/unicorn-hat) if you'd like more information before piping a URL straight to shell.
* [Python Twitter Tools](http://mike.verdone.ca/twitter/ "Python Twitter Tools (command-line client and IRC bot)"). Once installed, follow [these instructions](https://github.com/sixohsix/twitter/tree/master#working-with-oauth) to acquire the necessary Twitter OAuth keys for the username use wish to follow.

This code was copy-pasted together from examples and a bunch of StackExchange answers, with most of the "development" time spent with me trying to wrap my head around how to cast lists to string or integer. I've never written any Python before; pull requests which present better ways of doing things seen here are welcome!

### Configuration

Set `username` (line 34) to the Twitter handle your keys authenticate against. Tweets to this user will be processed.

## Usage

1. Tweet the target user with a hex colour code (as used in CSS): `@username #8a9a2a` will set the Unicorn HAT to the bright variant of Think Physics' theme green. The full 24-bit range `#000000` to `#FFFFFF` is available, though we can't speak to the colour accuracy of the LEDs. They're probably fairly terrible.
2. Tweet the target user with a Kelvin colour temperature: `@username 3400K` will set the Unicorn HAT to a warm orange-white. The available range is 1000-15000K.

At present, the code outputs diagnostics to STDOUT only. Stub code (from the Twitter Tools example) remains in place to tweet an acknowledgement in reply.

### Kelvin temperature

We're a physical sciences outreach project, so there had to be some physics in here somewhere. If only to justify the time investment. We'll write this up properly in a blog post, so for the moment:

* Here's [Wikipedia's primer on colour temperature](https://en.wikipedia.org/wiki/Color_temperature) and black body radiation curves.
* The Kelvin to RGB algorithm we're using is by [Tanner Helland, here](http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/ "How to Convert Temperature (K) to RGB: Algorithm and Sample Code &#8211; Tanner Helland (dot) com"), with the Python implementation referenced in the source itself.

## Future development

We plan two things:

1. Integration with a [Pi Camera](https://www.raspberrypi.org/products/camera-module/) module to take tree selfies and post them in response to input tweets.

2. Modification to replace the tree with a diffusing orb, and instrumentation so users can select a star temperature and have the orb glow the appropriate colour. Though colour conversion and perception are thorny subjects: see "[What colour is the Sun?](http://www.vendian.org/mncharity/dir3/starcolor/sun.html "What color is the Sun? - chromaticity above the atmosphere")" for an example.

We're quite likely to hack something together for Maker Faire UK in April 2016. Look for us there!
