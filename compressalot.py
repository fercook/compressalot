import os 
import sys
import zipfile

the_dir = sys.argv[1]
file_threshold = sys.argv[2]

def number_of_files(d):
	return sum([len(files) for r, d, files in os.walk(d)])

def compress_dir(d, files):
	dir_name = os.path.basename(os.path.normpath(d))
	print("compressin", dir_name)
	zipf = zipfile.ZipFile(d + '/content.zip', 'w', zipfile.ZIP_DEFLATED)
	for f in files:
		full_path = os.path.join(d, f)
		zipf.write(full_path, f)
		os.remove(full_path)
	zipf.close()



import os
from os.path import join, getsize
for root, dirs, files in os.walk(the_dir):
	if len(files) > 2:
		compress_dir(root, files)

