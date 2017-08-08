from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data:
            if data.count("\n") >= 1:
                print ">>> Multi-line Comment"
                print "".join(data)
            else:
                print ">>> Single-line Comment"
                print "".join(data)
                
    def handle_data(self, data):
        if data:
            if data != "\n":
                print ">>> Data"
                print "".join(data)
        
  
html = ""       
for i in range(int(raw_input())):
    html += raw_input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()