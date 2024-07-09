# JOB MATCHER

This repo is for a technical challenge. To run it you can use the requirements.txt and install the dependencies. I used VirtualEnv so my setup was as follows:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
flask --app main run -p 1988
```

To run the app  - open a browser and go to localhost:1988 - the root address will return the json object.

The test suite can be run using

```
python -m unittest
```

## Code Walkthrough

I wrote this code using flask so that it could be extended into an API with future iterations rather than a simple script. The main.py is a simple flask application that gets the members, attaches the jobs and returns it as a JSON object. It does this using the rest of the app that is a little more complex.

### api.py

This file deals with getting the data. using URLlib it gets the json and returns the members and jobs. This isn't tested and probably should be, it is also very hardcoded for the url that we provide. It would be nice to extend this so we could change the backend to return objects that are already hydrated rather than a JSON object for each and potentially hook up to a different API or database.

### member.py

A class that represents a single member. It hydrates the object from the JSON returned from the API and has a single method that assigns the jobs. It might be more intuitive to return the jobs from this method. It has limited tests and should have more but time is our enemy. The jobs are parsed through the jobs.py file

### jobs.py

A class that checks the location of a job posting and the title against the bio of a member. The title is a simple text lookup, it checks for a word that appears in both the bio and the title and returns a true if it finds a single word. This could lead to jobs that are not appropriate given two jobs may contain the same word but be quite different.

The location lookup checks against a list of locations we received from the location matcher class discussed below. It then checks that the location that we get from the job listing matches any of the words from the location matcher. Again this is a simple lookup and could lead to false positives for countries for example.

### location.py

This is the location matcher. It works by using phrases to glean which words might be actual locations in the text. It tries to make a list of included locations and those that the member may wish to exclude based on the language. This is a really naive way of getting a list of potential locations, it might have been better to use a NLP tool or even something simple like looking for upper case letters or a lookup dict might have been simpler and/or more precise.

### Various test files

There are tests that should show the criteria. I've made assumptions for example that someone moving from Edinburgh to London will only be interested in jobs in London - this may not be true but is tested as such. The tests get more thorough the lower in the code (so main is not tested but location.py has a number of tests). I have more or less only used data from the example data. There are more tests that I would have like to write to test edge cases and other things wording.
