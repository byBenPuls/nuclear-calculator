import tkinter as tk


def fahrenheit_to_celsius():
    """
    Конвертирует значение из градусов по Фаренгейту в градусы
    по Цельсию и выводит результат в ярлык lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


win = tk.Tk()  # Creating instance of Tk class
win.title("Nuclear Calculator")
win.iconbitmap('icon.ico')
win.resizable(False, False)  # This code helps to disable windows from resizing

window_height = 500
window_width = 900

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

frm_entry = tk.Frame(master=win)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Макет для рамки ввода температуры и ярлыка с символом Фаренгейта
# использует менеджер геометрии .grid().
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Создание кнопки-конвертера и ярлыка для вывода результата.
btn_convert = tk.Button(
    master=win,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=win, text="\N{DEGREE CELSIUS}")

# Настройка макета через менеджер геометрии .grid().
frm_entry.grid(row=0, column=0, padx=10)
frm_entry.grid(row=0, column=1, padx=10)
frm_entry.grid(row=0, column=2, padx=10)
frm_entry.grid(row=0, column=3, padx=10)
btn_convert.grid(row=0, column=4, pady=10)
lbl_result.grid(row=0, column=5, padx=10)
win.mainloop()
