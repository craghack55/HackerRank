from HTMLParser import HTMLParser
import re

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for i in attrs:
            print "-> " + i[0] + " > " + str(i[1])
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for i in attrs:
            print "-> " + i[0] + " > " + str(i[1])

parser = MyHTMLParser()

for i in range(int(raw_input())):
    parser.feed(raw_input())
