import webbrowser as web, wikipedia

choice = input("Press 1 for search on youtube\nPress 2 for search wikipedia page\n:- ")
if choice=='1':
    search = input("Search : ").split()
    if len(search)>1:
        search = '+'.join(search)
    else:
        search = ''.join(search)
    web.open(f'https://www.youtube.com/results?search_query={search}')
    
elif choice=='2':
    inp = input("Enter the page name : ")
    print('\n')
    try:
        result = wikipedia.page(inp)
        print(result.summary)
    except Exception as e:
        print(e)
    print()