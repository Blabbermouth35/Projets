import operator
import tkinter as tk

ops = {"+": operator.add, "-": operator.sub, "x": operator.mul, "/": operator.truediv}
"""
first_num = int(input(":"))
second_num = int(input(":"))
selected_operator = input(":")
def calculating():
result = ops[selected_operator](first_num, second_num)
"""
window = tk.Tk()
window.title("Calculator")
frame = tk.Frame(master=window, height=200, width=200)
frame.pack(fill=tk.BOTH, expand=True)
written_title = tk.Label(master=frame, text="CALCULATOR")
written_title.pack()
first_num_entry = tk.Entry(master=frame)
first_num_entry.pack()
second_num_entry = tk.Entry(master=frame)
second_num_entry.pack()
selected_operator_entry = tk.Entry(master=frame)
selected_operator_entry.pack()
result_label = tk.Label(master=frame, text="RESULTS WILL BE WRITTEN HERE")
result_label.pack()


def calculate():
    first_num = int(first_num_entry.get())
    second_num = int(second_num_entry.get())
    selected_operator = selected_operator_entry.get()
    result = ops[selected_operator](first_num, second_num)
    result_label["text"] = result


calculate_button = tk.Button(master=frame, text="Calculate", command=calculate)
calculate_button.pack()

window.mainloop()