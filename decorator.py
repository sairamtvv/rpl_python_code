

# myfunc()

def start_stop_printer(func):
    def wrapper():
        print("print started")
        func()
        print("print ended ")
    return wrapper

@start_stop_printer
def myfunc():
    print("pranav")

myfunc()
# wrapper = start_stop_printer(myfunc)
# wrapper()