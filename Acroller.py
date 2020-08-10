import os 


def createdir(directory): #create seprate directory for each new project
	if not os.path.exists(directory):
		print(f"Creating directory................{directory}")
		os.makedirs(directory)
def datalist(project_name, base_url):#create queue and crawled file if it is not already present
	queue= project_name + '/queue.txt'
	crawled= project_name + '/crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled,'')
		# print("hiii")
def write_file(path,data):
	f=open(path, 'w') #this w stands for write mode
	f.write(data)
	f.close()

def add_data(path,data):
	with open(path, 'a') as file: #a is for append mode
		file.write(data + '\n')

def delete_file(path): #delete files actcually overwrite
	with open(path, 'w'):
		pass #pass means do nothing

#this funtion is gonna read queue file and add the limks into set bcz set have only unique elements so no link will repeat itself
#this will increase the spped of crawler
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f: #rt is for reading mode
        for line in f:
            results.add(line.replace('\n', ''))
    return results
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")


