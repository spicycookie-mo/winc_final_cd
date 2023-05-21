# winc_final_cd
## Working as a user
•	Been working as root in previous exercises but wanted to create another user this time. I did that using sudo adduser but when I wanted to start redoing all the other steps I learnt that was not enough and I also needed to add to the sudoers file. 
•	Could not replicate the steps starting gunicorn with the same command because connection was already in use (by root) so I changed the port from 8000 to 8080	
•	Updated the WorkingDirectory in the farm.service file. Then restarted daemon restarted nginx and then I went back to /monica/farm/main.py and changed the message under /cow. I refreshed the page and the change was not visible. Nothing I did had any effect. My server is still running the farm created as root.
•	I run ps aux | grep gunicorn and there were two gunicorn processes running. Killed both of them and then restarted service. Changes were visible only while booting
•	Went back to farm.service and changed and ExecStart too to listen to 8080 and restarted daemon
•	Had to generate and add a new SSH key
## Steps took to implement CD:
- Once the app was set up and running on the server I created a git repository
- I then cloned the repository
- Within the clone I made changes to main (added a dog) and changed the yml file
- Generated a new ssh key and added it to my repository as deploy key
- Created secrets and used the private ssh key
- There were a milion steps in between and things i tried as nothing makes sense
- My test all pass but I can't deploy because I can't get past this error and i tried everything ssh: handshake failed: ssh: overflow reading version string
- - I run eval "$(ssh-agent -s)"
- - I run ssh-add ~/.ssh/deploy2 
- - I manually edited authorized_keys
- - I started all over several times
- - I don't know what else to do

### LE: It worked!! We have a dog! <3
###### ### Corrections made:
- was using wrong PORT secret (instead of default 22 I used 8080 because that is where I set-up the app; still not sure what 22 refers to)
- it was still not working because I was not using a PASSWORD for sudo restart gunicorn
- then it needed the -S option
- and it was actualy farm.service that I wanted to restart, where gunicorn is setup for this service

[![Deploy](https://github.com/spicycookie-mo/winc_final_cd/actions/workflows/deploy.yml/badge.svg)](https://github.com/spicycookie-mo/winc_final_cd/actions/workflows/deploy.yml)


### LE2: resubmit
Thank you for your feedback! I implemented the improvements that you suggested so I split the actions into two jobs and allowed user monica to run systemctl restart farm.service without password by modifying sudoers configuration file.
