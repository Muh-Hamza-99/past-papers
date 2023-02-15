class greeting:
    def hello(self, name = None):
        if name is not None:
            print(f"Hello {name}")
        else:
            print("Hello")
greeting = greeting()
greeting.hello()