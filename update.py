# This is my python script to update my website with jemdoc
import sys
import os
print sys.version
files = ['index', 'research', 'teaching', 'talk_videos']

for i in files:
	os.system('python jemdoc.py '+i)
