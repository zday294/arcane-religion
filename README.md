# Oddly Specific Calculator

The problem with being a nerd in two different fields is that occasionally you ened up using your knowledge in one field to benefit you in another field. This project is just a really complicated way for me to figure out how much time and money I'm going to be wasting (in game) on learning religious spells. For now, the goal is to just run it as a script and that takes a bunch of csvs in and outputs another csv for me to read. Maybe later I'll add features to make it more interactable, but for now that's really all I need to do to get the calculations I need done quickly and repeatably.

## Why did you make this? What's this thing even trying to do?

That's a long story, and givent that most people who read a README are just trying to get an app running, I have elected to move that long story to [LONGSTORY.md](LONGSTORY.md). It will explain a lot, including what prompted all this, the process I'm attempting to represent with the application, a description of previous attempts to quantify this process, and a brief explanation of the math going on here (an explanation from someone who barely understands it himself mind you, so it will be like one sentence followed by a link to the Wikipedia article about the math).

## Why are there C files in here?

I need to use a random number generator *a lot* in here, so I decided to use C to speed things up by doing a lot of the heavily repeated calculations in there. Also, it tests if I actually learned anything in college.

## Install and Run Instructions

Fundamental thing you need to understand is that I made this thing on a Mac for pretty much exclusively myself and writing this README is more an exercise in documentation than intent to make full instructions. As such, instructions are written for Mac and if you want to run this on a different platform, consider this an opportunity to explore learning how to port an application to your system.

### Python

First, make sure you have Python 3 installed. It's kind essential.

This project uses a yaml library called `pyyaml`. You can install it with the command `pip3 install pyyaml` on Mac. This library is necessary to read the config file. Yes this project *is* how I learned that YAML's resemblance to Python with it's use of indentation as a rigid means of separation

### C Stuff

If you have the `make` utility installed, you should be able to just use that. The commands are `make base` and `make shared`. Together, these will build the C project as a shared object file.

If you don't have the `make` utility installed, either install it or use the command under the listings `base` and `shared` in the Makefile.

### Supplementary Files

#### config.yml

`config.yml` has a few fields in it that need to be filled out for the application to run properly. These include

- `simulations` : The number of times to run the simulation for each player/character
- `attempts` : The maximum number of attempts before giving up in a single simulation
- `spell-table-file`: TODO: explain this chart elsewhere first
- `player-stats-file` : The name of the input file with a list of each player you wish to do the calculation for. See below for required fields
- `output-gold-file` : The desired name of the output file where the table for the gold costs will be written. [I should add a default later]
- `output-time-file` : Same as gold file but for time.

#### spell-table-file

The spell table file represents the table of costs and difficulties for learning the spells. 

### Running the Application

Once the `config.yml` file has been created along with all other supplementary files, run the command `python3 compute-arcane-religion.py` in the same directory as your supplementary files and `arclib.so`.

### Interpreting the Results

Uh... I'll get to this in a bit.

### Conclusion

If I didn't send this to you directly, *why are you here?* Also I hope you enjoyed this however you did come across it. Will I make something like this again? Possibly. Depends on if I get given a sufficiently interesting problem that can be solved with a little math and a couple files of code.

Aur Revoir or however you spell that.
