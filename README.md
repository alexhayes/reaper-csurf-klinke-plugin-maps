# REAPER CSURF Klinke Plugin Maps

This is a collection of plugin XML map files to use with klinke's amazing [MCU control surface extension](https://bitbucket.org/Klinkenstecker/csurf_klinke_mcu/src) for [Reaper](https://reaper.fm).

I have mapped many UAD plugins, Plugin Alliance, Softube, Soundtoys, DMG Audio, Slate, Cytomic, Ohm Force and others.

These should work on both a Mackie MCU and a BCF2000.

Note that klinke's MCU control surface extension currently only works with Windows. 

## Usage

Once you have klinke's MCU control surface extension working then all you need to do is copy the plugin map XML files from this repository onto your computer, restart Reaper and you should be good to go.

For me, on Windows 11, the plugin map XML files go in `C:\Users\me\Documents\Reaper\MCU\PlugMaps` however this will likely be different depending on how you've installed Reaper (and of course if you're using Linux, Mac or Windows).

## Conventions

I've tried to follow a few conventions when creating these mapping files which don't always map to the left/right layout of the plugin.

Where I've deviated is when there are so few parameters that it makes more sense to follow the left/right layout of the plugin.

If people want to contribute, it would be nice if they can adhere to the following "conventions" however of course its not essential.

### Pages

I've tried to separate pages into logical groups so that the controls are not too cluttered.

### Power

Where possible I've tried to put the power (or bypass/on/off) switch on the top right hand VPOT.

### Input/Output Levels

On plugins that have input/output levels I've generally mapped these as follows:

- Input: mapped to the first fader
- Output: mapped to the last fader

Sometimes I deviate from this for plugins like channel strips where quite often I'll place the input/output on faders 7 & 8 for certain pages (such as, compression and gate pages).

### EQ Frequency/Gain/Q

I've tried to adhere to the same layout for EQ plugins so that:

- Frequency: is the left most fader
- Gain: is the fader to the right of Frequency
- Q: is to the fader to the right of Gain OR is operated by a VPOT above Gain.

I've deviated from this convention for plugins where it was more logical to follow the layout of the plugin, such as UAD's Neve 1073.

## Step Generator

Quite often I map the `Q` parameter of an EQ to a VPOT so that you can fit all 4 EQ bands of a channel strip on 8 faders (4 faders for freq, 4 for gain, 4 VPOTs for enable/disable band and 4 to control `Q`).

The problem is when in `Learn` mode within the Klinke Plugin Mapping Editor if you're mapping a continuously variable control to a VPOT there can be hundreds of step values mapped. This can make turning the control very slow.

To workaround this I've included a script called `step_generator.py` which can be used to generate the `<STEP/>` XML nodes for a particular parameter.

```bash
python step_generator.py command
```

### `step-size` command

The `step-size` command allows for a fixed step size from a start and stop value. 

For example: each EQ band on Plugin Alliance's bx_console AMEK 9099 channel strip plugin has a `Q` param which is continuously variable from `0.65` to `2`. You could use the step generator script to generate steps in `0.1` increments as follows;

```bash
python step_generator.py step-size 0.1 0.65 2
```

Outputs;

```xml
       <STEP value="0" short="0.65" long="0.65"/>
       <STEP value="0.074074" short="0.75" long="0.75"/>
       <STEP value="0.14815" short="0.85" long="0.85"/>
       <STEP value="0.22222" short="0.95" long="0.95"/>
       <STEP value="0.29630" short="1.05" long="1.05"/>
       <STEP value="0.37037" short="1.15" long="1.15"/>
       <STEP value="0.44444" short="1.25" long="1.25"/>
       <STEP value="0.51852" short="1.35" long="1.35"/>
       <STEP value="0.59259" short="1.45" long="1.45"/>
       <STEP value="0.66667" short="1.55" long="1.55"/>
       <STEP value="0.74074" short="1.65" long="1.65"/>
       <STEP value="0.81481" short="1.75" long="1.75"/>
       <STEP value="0.88889" short="1.85" long="1.85"/>
       <STEP value="1" short="2" long="2"/>
```

You can then copy and paste this output into the appropriate place within the XML file for your plugin map.


### `steps` command

The `steps` command allows for a fixed number of steps between two values. 

Each EQ band on Plugin Alliance's bx_console AMEK 9099 channel strip plugin has a `Q` param which is continuously variable from `0.65` to `2`. If we wanted to control this param with eleven step rotations of a VPOT on the MCU we could do the following;

```bash
python step_generator.py steps 11 0.65 2
```

Outputs;

```xml
       <STEP value="0" short="0.65" long="0.65"/>
       <STEP value="0.1" short="0.785" long="0.785"/>
       <STEP value="0.2" short="0.920" long="0.920"/>
       <STEP value="0.3" short="1.055" long="1.055"/>
       <STEP value="0.4" short="1.190" long="1.190"/>
       <STEP value="0.5" short="1.325" long="1.325"/>
       <STEP value="0.6" short="1.460" long="1.460"/>
       <STEP value="0.7" short="1.595" long="1.595"/>
       <STEP value="0.8" short="1.730" long="1.730"/>
       <STEP value="0.9" short="1.865" long="1.865"/>
       <STEP value="1" short="2" long="2"/>
```

You can then copy and paste this output into the appropriate place within the XML file for your plugin map.

## Author

Alex Hayes (aka ''plant-on'' on the reaper forums)

## License

Copyright (c) 2011 Alex Hayes Dual licensed under the MIT and GPL licenses.
