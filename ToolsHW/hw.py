import sys
import webbrowser

RICKROLL_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

error_count = 0


def input_math() -> None:
    global error_count
    while True:
        user_input = input("1 times 1 = ? ")
        if user_input == "1":
            open_video()
            break
        elif user_input == "exit":
            sys.exit()
        else:
            print("Wrong! Try again.")
            error_count += 1


def open_video() -> None:
    webbrowser.open(RICKROLL_URL)
    print("Rickroll incoming...")


if __name__ == '__main__':
    input_math()
