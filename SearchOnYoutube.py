import webbrowser as web
search = input("Search : ").split()
if len(search)>1:
    search = '+'.join(search)
else:
    search = ''.join(search)
web.open(f'https://www.youtube.com/results?search_query={search}')