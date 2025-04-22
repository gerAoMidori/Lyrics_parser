from pynput import keyboard
import pyautogui
import pyperclip
import time

listener = None  # Placeholder
pressed = 0


def on_press(key):

    global listener
    global pressed


    lyrics = data()
    
    try:

        if key.char == 'a':
            time.sleep(0.1)
            print("You pressed the 'A' key!")
            print(lyrics[pressed])
            paste_text(lyrics[pressed])
            pressed += 1

        if key.char == 'q':
            print("Stopping listener...")
            listener.stop() 

    except AttributeError:
        pass

    if pressed == len(lyrics):
        listener.stop() 

def data():
    # I used src/lyrics.txt instead of lyricrs.txt because I didn't trust in the right repository in vscode
    with open("src/lyrics.txt", 'r', encoding="utf-8") as f:
        lyrics = f.readlines()
    return lyrics

def paste_text(text):
    # Text you want to paste
    # text = "안녕하세요! 😊✨ This is a test — 좋아요!. I'm happy to see that it's working"
    
    #Take safely copies Unicode text  to the clipboard.
    pyperclip.copy(text)

    # Select to whole zone text and paste the lyric

    pyautogui.press("backspace")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("backspace")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()