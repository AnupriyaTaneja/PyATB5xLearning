def add_before_ui_after_ui(func): # in place of func test_ui can be used, but this is industry standard
    def wrapper():
        print("Before running the test case")
        print("After running the test case")
        func()
        print("Ending the running UI TC")
        print("Quit the browser")
    return wrapper()

@add_before_ui_after_ui
def test_ui():
    print(">> I will test the UI")