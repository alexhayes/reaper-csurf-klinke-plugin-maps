# REAPER CSURF Klinke Plugin Maps

This is a collection of plugin xml map files to use with klinke's MCU control surface extension.

I have mapped most of the UAD plugins and some Softube, Soundtoys and others.

I use a BCF2000 thus I haven't tested on a Mackie MCU however I imagine that the mapping works the same.

# Conventions

I've tried to follow a few conventions when creating these mapping files which don't always map to the left/right layout of the plugin.

Where I've deviated is when there are so few parameters that it makes more sense to follow the left/right layout of the plugin.

If people want to contribute, it would be nice if they can adhere to the following "conventions" however of course its not essential.

## Pages

I've tried to separate pages into logical groups so that the controls are not too cluttered.

## Power

Where possible I've tried to put the power (or bypass/on/off) switch on the top right hand VPOT.

## Input/Output Levels

On plugins that have input/output levels I've generally mapped these as follows:

- Input: mapped to the first fader
- Output: mapped to the last fader

## EQ Frequency/Gain/Q

I've tried to adhere to the same layout for EQ plugins so that:

- Frequency: is the left most fader
- Gain: is the fader to the right of Frequency
- Q: is to the fader to the right of Gain

I've deviated from this convention for plugins where it was more logical to follow the layout of the plugin, such as UAD's Neve 1073.

# Author

Alex Hayes (aka ''plant-on'' on the reaper forums)

# License

Copyright (c) 2011 Alex Hayes Dual licensed under the MIT and GPL licenses.