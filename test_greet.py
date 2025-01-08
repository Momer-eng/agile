from greet import greet  # Import the function from your script

def test_greet(capfd):
    # Call the function
    greet("moha")
    
    # Capture the printed output
    captured = capfd.readouterr()
    
    # Check if the output matches the expected string
    assert captured.out == "Bonjour, moha\n"