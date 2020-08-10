from urllib.request import urlopen
from check_link import LinkFinder
from domain import *
from Acroller import *


class Snake:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Snake.project_name = project_name
        Snake.base_url = base_url
        Snake.domain_name = domain_name
        Snake.queue_file = Snake.project_name + '/queue.txt'
        Snake.crawled_file = Snake.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('Snake is', Snake.base_url)

    # Creates directory and files for project on first run and starts the Snake
    @staticmethod
    def boot():
        createdir(Snake.project_name)
        datalist(Snake.project_name, Snake.base_url)
        Snake.queue = file_to_set(Snake.queue_file)
        Snake.crawled = file_to_set(Snake.crawled_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Snake.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Snake.queue)) + ' | Crawled  ' + str(len(Snake.crawled)))
            Snake.add_links_to_queue(Snake.gather_links(page_url))
            Snake.queue.remove(page_url)
            Snake.crawled.add(page_url)
            Snake.update_files()

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Snake.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Snake.queue) or (url in Snake.crawled):
                continue
            if Snake.domain_name != get_domain_name(url):
                continue
            Snake.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Snake.queue, Snake.queue_file)
        set_to_file(Snake.crawled, Snake.crawled_file)
