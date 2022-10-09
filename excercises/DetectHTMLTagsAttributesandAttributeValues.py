from html.parser import HTMLParser
class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print("->", ele[0], ">", ele[1])


html=""
for i in range(int(input())):
    html+=input().strip()+"\n"
parser=Parser()
parser.feed(html)
parser.close
