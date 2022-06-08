CSV Parsing Problem

How to run:

In a Linux environment (I am using Ubuntu), run the command:

`python3 [full/path/to]main.py [input file] [output file]`

for example:

`python3 main.py sample.csv testout.csv`

The input and output files need to/will be in the same folder as the python file.
For best results, I recommend running the above command from the folder where the file is located.

Python packages included in this file are:
- typing
- click
- dateutil
- pytz

All but click should be in the standard Python library, but any Python package maintained on PyPi can be installed with:

`pip install [package-name]`

Notes of my thought process:
- At the end of the .py file you can see how I organized my thoughts on how to approach the structure of the method.
- I generally use type hinting to help me keep my code organized, as I come from a Java/strongly typed background, although in "first pass" coding scenarios, a bit like this, sometimes it falls by the wayside, so it may be hit and miss throughout this sample.

Some aspects I would like to solve/consider further include:
- The "computer" decimal precision printing on TotalDuration for some entries.
- Proper Unicode validation. Python appeared to be doing this for me, but I'm not sure if that's Python doing that, or my environment (I'm using VSCode through WSL). Python appears to handle unicode pretty seamlessly, but this is an aspect I'm fairly unfamiliar with and would like to spend more time with.
- Date and time validation, and properly producing an error, as well as removing the line. My thought for approaching this is to actually save the whole line in a buffer, and then just kick out of that iteration of the for loop and not write the buffer to the file, if I run into a formatting issue. I certainly could do this, just a matter of time and ensuring that I don't spend more than the requested 4 hours.
- Addressing that currently in the command line the "python" command must still be invoked. I would love to figure out how to work around that, and essentially make this an executable of some type.
- And further extension of the normalizer to ensure that if the timestamps already have time zone information, it doesn't override.