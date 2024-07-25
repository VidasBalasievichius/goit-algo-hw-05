def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "The command requires additional input."
    return inner

contacts = {}

@input_error
def add_contact(args):
    if len(args) < 2:
        raise ValueError
    name = args[0]
    phone = args[1]
    contacts[name] = phone
    return "Contact added."

@input_error
def list_all_contacts(args):
    if args:
        raise IndexError
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {contacts[name]}" for name in contacts)

@input_error
def find_phone(args):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"

def handle_command(command):
    command_parts = command.strip().split(maxsplit=1)
    if not command_parts:
        return "Enter a command."

    cmd = command_parts[0].lower()
    args = command_parts[1].split() if len(command_parts) > 1 else []

    if cmd == "add":
        result = add_contact(args)
    elif cmd == "all":
        result = list_all_contacts(args)
    elif cmd == "phone":
        result = find_phone(args)
    else:
        result = "Command not recognized."

    return result

while True:
    command = input("Enter a command: ")
    if command.lower() == "exit":
        break
    print(handle_command(command))
