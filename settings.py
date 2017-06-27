# Establish List that functions can be registered to
my_commands = {}


def register(cmd):
    my_commands[cmd.__name__] = cmd
    return cmd