def tagMaker(func):
    def wrapper(*args, **kwargs):
        print('<div>')
        func(*args, **kwargs)
        print('</div>')

    return wrapper


@tagMaker
def printText(text):
    print(text)