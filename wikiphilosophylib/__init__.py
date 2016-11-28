import wikipedia
from bs4 import BeautifulSoup
import re
import sys
import contextlib
import sys
import cStringIO

@contextlib.contextmanager
def nostderr():
    save_stderr = sys.stderr
    sys.stderr = cStringIO.StringIO()
    yield
    sys.stderr = save_stderr

def next_link(cur, done):
    try:
        g = wikipedia.page(cur).html()
    except wikipedia.exceptions.DisambiguationError as e:
        for op in e.options:
            if op not in done:
                g = wikipedia.page(op).html()
                break
    soup = BeautifulSoup(re.sub(r'\([^)]*\)', '', g), "html.parser")
    for para in soup.findAll("p"):
        flag = False
        for link in para.findAll("a"):
            flag = True
            if link.get("href").startswith("/wiki/") and link.get("title") not in done and link.contents[0].islower():
                return link.get("title")

def main():
    if len(sys.argv) > 1:
        start = sys.argv[1]
    else:
        start = wikipedia.random()
    done = set()

    while start != "Philosophy":
        done.update([start])
        sys.stdout.write(start)
        sys.stdout.flush()
        with nostderr():
            start = next_link(start, done)
        if start is None:
            print("\nNo more links")
            exit()
        sys.stdout.write(" -> ")
        sys.stdout.flush()

    print(start)
    print("Length: " + str(len(done) + 1))
