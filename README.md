# New committer:
In order to make changes in this repository please invoke the following commands:



#

# clone the repository:
git clone https://github.com/kobybm/tikalTest.git && cd tikalTest

# make some changes on JustAfile
echo "$(date) $RANDOM $RANDOM" > JustAfile

# Commit your change
git commit -am "Random commit"

# Push your changes
git push origin master

# Got to Jenkins via chrome
http://[JENKINS IP]:8080

# View your git commit CI flow on "CI_web" job
The CI flow does the following:
- Poll SCM - Waits for new git pushes and auto-start a new build 
- invoke unitest.sh - check code get 200 OK with a string
- build the docker image (+ save the image On localhost)
- deploy the docker image with ansible (On localhost)

# You can view the app at: http://[JENKINS IP]/tikal
You will see there your name + commit ID + Jenkins Build number
