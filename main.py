import threading
from queue import Queue
from snake import Snake
from domain import *
from Acroller import *

print(
	"""

  ___                 _ _           
 / _ \               | | |          
/ /_\ \ ___ _ __ ___ | | | ___ _ __ 
|  _  |/ __| '__/ _ \| | |/ _ \ '__|
| | | | (__| | | (_) | | |  __/ |   
\_| |_/\___|_|  \___/|_|_|\___|_|   

Designed by- Asura
IG account- @error_404_unavilable
this is open source project,your are free to contribute and modify.
Happy hacking.                                                                       
	""")
PROJECT_NAME= 'asura'
HOMEPAGE='https://tecahead.com/'
DOMAIN_NAME =get_domain_name(HOMEPAGE)
QUEQUE_FILE =PROJECT_NAME + '/queue.txt'
CRAWLED_FILE=PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS =8
queue = Queue()
Snake(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()



def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()



def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    queued_links = file_to_set(QUEQUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()
