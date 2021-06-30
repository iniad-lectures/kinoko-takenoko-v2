import re

test = [
    'For detail check https://moocs.iniad.org!',
    'this is https://facebook.com lalala',
    'this is https://facebook.com lalala and https://moocs.iniad.org haha',
    '[text] something - https://www.myurl.com/test1/ lorem ipsum https://www.myurl.com/test2/ - https://www.myurl.com/test3/ marker needle - some more text at the end',
]

for case in test:
    result = re.sub(r"(https?://)([\w.]+)(\.[\w/]+)", r'<a href="\g<0>">\g<0></a>', case)
    result2 = re.search(r"(https?://)([\w.]+)(\.[\w/]+)", case)
    result3 = re.findall(r"(https?://)(\w+)(\.[\w/]+)", case)
    print(result, end='\n\n')
    # print(result2)
    # print(result3)