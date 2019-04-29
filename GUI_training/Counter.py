class Counter():
    global count_label
    
    
    def __init__(self):
        self.num = 0
    
    def up(self):
        self.num += 1
        count_label["text"] = str(counter.num)
    def down(self):
        self.num -= 1
        count_label["text"] = str(counter.num)
    def clear(self):
        self.num = 0
        count_label["text"] = str(counter.num)
    def exit(self):
        root.destroy()
        exit

import tkinter as tk

root = tk.Tk()
root.title("Counter")
root.geometry=("1280x1960")

counter = Counter()

count_label = tk.Label(root, text=str(counter.num))
count_label.grid( row=0, column=1 )

control_frame = tk.Frame(root)
control_frame.grid(row = 1, column = 1)

up_button = tk.Button(control_frame, text = "UP", command = counter.up)
up_button.grid(row = 1, column = 2)

down_button = tk.Button(control_frame, text = "DOWN", command = counter.down)
down_button.grid(row = 2, column = 2)

clear_button = tk.Button(control_frame, text = "CLEAR", command = counter.clear)
clear_button.grid(row = 3, column = 2)

exit_button = tk.Button( control_frame, text="EXIT", command=counter.exit )
exit_button.grid( row=4, column=2 )

count_label["text"] = str(counter.num)

root.mainloop()

