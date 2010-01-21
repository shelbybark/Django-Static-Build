Django Static Build
===================

Django Static Build is a basic django project that I use to create "static builds" with my job. Instructions for outputting the static builds as html docs below:

Instructions for static dump
----------------------------

The basic command is: 

    ./manage.py staticdump

You will need to have the manage.py runserver running on your machine for the command to work. The default server it looks for is http://127.0.0.1:8000, but you can pass in your own host and port with the --host and --port parameters.

It's very basic. The script will look at all the urls set up in the urls.py file. and try creating the files based on that. It has no error handling, so, the urls must all work. Also, since the need I had did not include any real views, anything other than a "direct_to_template" probably would not work. It also attempts to copy over the contents of "/media/" which would reside in the project folder.

