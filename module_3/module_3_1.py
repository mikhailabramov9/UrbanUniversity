calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    len_ = len(string)
    u = string.upper()
    l = string.lower()
    string = (len_, u, l)
    print(string)
    return string

def is_contains(string, list_of_search):
    count_calls()
    for i in list_of_search:
        if string == i:
            print(True)
        else:
            break
        print(False)

string_info("banana")
string_info("переворот с переподвыподвертом")
is_contains("banana", ["banana", "milk", "carrot"])
is_contains("apple", ["banana", "papa", "mama"])
print(calls)