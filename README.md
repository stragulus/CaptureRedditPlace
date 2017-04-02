# CaptureRedditPlace
Save Reddit's /r/place canvas to a PNG file

# Usage

On a *nix system (OSX, linux), in a terminal, change to the directory where you checked out this repo. E.g. it should contain requirements.txt.

From there, create a python2 virtual environment using the commands below. Note that one of the dependencies is Pillow, a python imaging library, which needs to compile code and thus requires more system depencies.

    virtualenv ~/opt/capture_the_place
    source ~/opt/capture_the_place/bin/activate
    pip install -r requirements.txt
    
Now, simply invoke the python code to fetch the /r/place canvas into a PNG file:

    python2 ./capture_reddit_place.py
    
This will generate a file in your current working directory with the current date and time as part of the filename.

If you want to do this every minute, you can do something like this:

    while : ; do python2 ./capture_reddit_place.py ; sleep 60 ; done
    
Enjoy!
