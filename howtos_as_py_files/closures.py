# Python 3.x
# sr 11/04/2013
# closures
#

def create_message(msg_txt):
    def _priv_msg(message):     # private, no access from outside
        print("{}: {}".format(msg_txt, message))
    return _priv_msg            # returns a function

new_msg = create_message("My message")
# note, new_msg is a function

new_msg("Hello, World")
# prints: "My message: Hello, World"

# print(dir(create_message.__closure__))
