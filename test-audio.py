# option 1
import playsound

playsound.playsound('avalanche_goal_horn.mp3', True)

# option 2
import os

os.system("mpg123 " + "avalanche_goal_horn.mp3")

