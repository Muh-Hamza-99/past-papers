class Greeting:
    def hello(self, first_name=None, last_name=None):
        if not first_name and not last_name:
            print("Hello!")
        elif first_name and last_name:
            print(f"Hello {first_name} {last_name}!")
        else:
            print(f"Hello {first_name}!")

new_greeting = Greeting()
new_greeting.hello("Muhammad")