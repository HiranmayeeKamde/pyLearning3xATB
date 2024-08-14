def outer_function():
    var = 30

    def inner_function():
        print(var)

    inner_function()


#inner_function()  # --NameError: name 'inner_function' is not defined.
outer_function()
