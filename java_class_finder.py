import sys
import os
import re

def findJavaFiles(root_dir) :

	classes = 0
	# compile the regex
	pattern = re.compile("\\s*(public|private)*\\s+(class|interface)\\s+(\\w+)\\s+((extends\\s+\\w+)|(implements\\s+\\w+( ,\\w+)*))?\\s*\\{") # everything
	
	#pattern = re.compile("\\s*(public|private)\\s+(class|interface)\\s+(\\w+)\\s+((extends\\s+\\w+)|(implements\\s+\\w+( ,\\w+)*))?\\s*\\{") # no inner classes
	#pattern = re.compile("\\s*(public|private)\\s+(class)\\s+(\\w+)\\s+((extends\\s+\\w+)|(implements\\s+\\w+( ,\\w+)*))?\\s*\\{") # no inner classes or interfaces
	#pattern = re.compile("\\s*(public)\\s+(class)\\s+(\\w+)\\s+((extends\\s+\\w+)|(implements\\s+\\w+( ,\\w+)*))?\\s*\\{") # no inner classes or interfaces or private classes (add a break statement on line 31 just to be sure)
	
	
	# go through all directories and files in the args directory
	for path, directories, files in os.walk(root_dir) :
		
		# for each file, if it's a .java file then open it
		for file_name in files :
			
			if file_name.endswith(".java") :
				
				file = open(os.path.join(path, file_name))
				
				# go through every line in the file looking for a regex match
				for line in file :
					
					if pattern.match(line) :
						
						classes += 1
				
		
		# recursively iterate through subdirectories
		for subdirectory in directories :
			
			classes += findJavaFiles(subdirectory)
			
	
	return classes
	
		
		
if(len(sys.argv) < 2 or len(sys.argv) > 2) :
	
	print("Invalid arguement. Please pass in the root directory of the unzipped Java src files.")
	
else :
	
	root_folder = sys.argv[1]
	number_of_java_files = findJavaFiles(root_folder)
	print("Number of java classes found was " + str(number_of_java_files))