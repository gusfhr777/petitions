import chromedriver_autoinstaller, re, os
def getpath():
    try: os.mkdir('./chromedriver_autoinstaller')
    except: pass
    try:
        a=re.compile("([\d]*)[.]?").search(chromedriver_autoinstaller.get_chrome_version()).group(1)
        os.mkdir("./chromedriver_autoinstaller/"+a)
    except:pass
    chromedriver_autoinstaller.install()
    return a