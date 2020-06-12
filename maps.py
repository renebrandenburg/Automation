import webbrowser, sys, pyperclip 

sys.argv # ['maps.py', '229' 'Caan van Necklaan']

# check if command line value are passed 
if len(sys.argv) > 1:
    # ['maps.py', '229' 'Caan van Necklaan'] -> '229 Caan van Necklaan'
    adress = ''.join(sys.argv[1:])
else:
    adress = pyperclip.paste()

# https://www.google.com/maps/place/<adress>
webbrowser.open('https://www.google.com/maps/place/' + adress)


