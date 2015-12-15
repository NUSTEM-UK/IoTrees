# Internet of Trees

Whatever the 'Next Big Thing' is, there's apparently going to be an Internet Of them. We think at least some of the Things should be trees -- Christmas trees. With sparkly lights.

This code drives coloured lights from a Twitter stream. It's a ghastly hack, but in initial testing it mostly works. It's also our first Python code, so, you know, be gentle.

## Hardware

To replicate Think Physics' IoTree, you'll need:

1. A tree. We built [this design](http://www.instructables.com/id/Makedo-Christmas-tree/ "Makedo Cardboard Christmas tree: 2015 UPDATE") from Makedo on Instructables. Makedo is a terrific cardboard construction system with which you can quickly lash together big structures. We love it.
2. A Raspberry Pi. We used a Pi2 backed onto a Pi touchscreen, in a Pimoroni stand. We'd planned to use a Pi Zero, but couldn't get our hands on one. The Pi needs to be on a network; we used a WiFi dongle, since plugging things into our university network is frowned upon.
3. A Pimoroni Unicorn HAT, which is a nifty little 8x8 array of individually-addressable RGB LEDs.

## Software

This code was copy-pasted together from example code and a bunch of StackExchange answers, then I spent a bunch of time trying to wrap my head around how to cast lists to strings and integers. There are more elegant ways of achieving the same results. At least, I hope there are, or all the good things I've heard about Python turn out to be complete fibs.

TODO: complete this README.