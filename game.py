import PySimpleGUI as sg
import random

def play_guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    layout = [
        [sg.Text("Вгадайте число від 1 до 100.")],
        [sg.InputText(key="input_guess"), sg.Button("Вгадати")],
        [sg.Text("", size=(20, 1), key="output_message")]
    ]

    window = sg.Window("Гра 'Вгадай число'", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Вгадати":
            try:
                user_guess = int(values["input_guess"])
            except ValueError:
                window["output_message"].update("Введіть коректне число.")
                continue

            attempts += 1

            if user_guess < secret_number:
                window["output_message"].update("Загадане число більше. Спробуйте ще раз.")
            elif user_guess > secret_number:
                window["output_message"].update("Загадане число менше. Спробуйте ще раз.")
            else:
                sg.popup_ok(f"Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб.")
                break

    window.close()

if __name__ == "__main__":
    play_guess_the_number()
