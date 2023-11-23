import queue
import sys
import threading
import time

from Aggregator import Aggregator

from Article import Article


def worker(q: queue.Queue):
    # repeat every 5 minutes
    sleep = 60 * 5
    a = Aggregator()
    articles = set()
    while True:
        new = a.get_articles()
        for i in new:
            if i.title not in articles:
                articles.add(i.title)
                q.put(i)
        time.sleep(sleep)


def main():
    q = queue.Queue()
    background_thread = threading.Thread(target=worker, args=[q], daemon=True)
    try:
        background_thread.start()
        while True:
            if not q.empty():
                a: Article = q.get()
                print(a)
                print()
            else:
                time.sleep(0.5)
            print(end="", flush=True)
    except (KeyboardInterrupt, SystemExit):
        print("Exiting program...")
        # kills all daemons
        sys.exit()


if __name__ == "__main__":
    main()
