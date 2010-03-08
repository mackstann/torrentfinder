torrentfinder
=============

torrentfinder is a small script for running multiple searches on The Pirate Bay
and aggregating the results into a single HTML page.

Dependencies
============

The Python [lxml] library is required.  In Debian/Ubuntu, install it with
`apt-get install python-lxml`.  Otherwise, try `easy_install lxml`.

[lxml]: http://codespeak.net/lxml/

Usage
=====

Run it like this:

    $ python main.py my-input-file

*my-input-file* may be a text file with a search phrase on each line, or it may
be a CSV file, where the first column is assumed to be the search phrase.
Because the file is treated as CSV, make sure you quote strings that contain
commas.

The searches will be executed and the results written to a file called
*output.html* in the current directory.  Note that the script is fairly slow to
run; this is intentional.  TPB are providing a free service and it's not nice
to hammer their servers, so the script waits for a few seconds between each
request.

Copyright Information
=====================

Written by Nick Welch in 2010.  
No copyright.  This work is dedicated to the public domain.  
For full details, see http://creativecommons.org/publicdomain/zero/1.0/
