import tkinter as tk
from tkinter import TclError, ttk


def create_block_of_text(container, text):
    frame = tk.Frame(container, bd=4, relief="raised",
                     highlightbackground="#6E6666", highlightthickness=3)
    ttk.Label(frame, text=text).grid(column=0, row=2, sticky=tk.W)
    return frame

def create_input_frame(container,ldr_number):


    frame = tk.Frame(container, bd=4, relief="raised",
                     highlightbackground="#6E6666", highlightthickness=3)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=2)


    # Find what
    ttk.Label(frame, text='LDR '+ str(ldr_number)).grid(column=0, row=0, sticky=tk.W)
    ttk.Label(frame, text='Mooring detail 1:').grid(column=0, row=1, sticky=tk.W)
    keyword = ttk.Entry(frame, width=10)
    keyword.focus()
    keyword.grid(column=1, row=1, sticky=tk.W)

    # Replace with:
    ttk.Label(frame, text='Mooring detail 2:').grid(column=0, row=2, sticky=tk.W)
    replacement = ttk.Entry(frame, width=10)
    replacement.grid(column=1, row=2, sticky=tk.W)

    ttk.Label(frame, text='Mooring detail 3:').grid(column=0, row=3, sticky=tk.W)
    replacement = ttk.Entry(frame, width=10)
    replacement.grid(column=1, row=3, sticky=tk.W)

    ttk.Label(frame, text='Mooring detail 4:').grid(column=0, row=4, sticky=tk.W)
    replacement = ttk.Entry(frame, width=10)
    replacement.grid(column=1, row=4, sticky=tk.W)

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='Disable y',
        variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=5, sticky=tk.W)

    # Wrap Around checkbox
    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text='Enable x',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=6, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame



def create_canvas_frame(container, x, y):
    frame = tk.Frame(container,  bd=4, relief="raised",
                     highlightbackground="#6E6666", highlightthickness=3)
    # Input number of moorings
    canvas_width = x
    canvas_height = y
    python_green = "#476042"
    mainCanvas=tk.Canvas(frame, width=canvas_width,
           height=canvas_height)
    points = [50, 40, 10, 10, 40, 50, 10, 90, 50, 60, 90, 90, 60, 50, 90, 50]

    mainCanvas.create_polygon(points, outline=python_green,
                     fill='yellow', width=3)
    mainCanvas.grid(column=0, row=0, sticky=tk.W)
    return frame


def create_input_mooring_number_frame(container):
    frame = tk.Frame(container, bd=4, relief="raised",
                     highlightbackground="#6E6666", highlightthickness=3)
    # Input number of moorings
    ttk.Label(frame, text='Mooring number:').grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=10)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    return frame

def create_main_window():
    root = tk.Tk()
    root.title('LDR Tool')
    root.geometry('1200x800')
    root['background'] = '#6E6666'
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    # layout on the root window
    root.columnconfigure(0, weight=0)

    mooring_frame = create_input_mooring_number_frame(root)
    mooring_frame.grid(column=0, row=0, padx=(10, 10), pady=(5, 5))

    block_of_text_frame = create_block_of_text(root,"LDR Specification")
    block_of_text_frame.grid(column=0, row= 1, columnspan = 3, padx=(130), pady=(5, 5))

    canvas_frame = create_canvas_frame(root, 50, 50)
    canvas_frame.grid(column=0, row=4, padx=(10, 10), pady=(5, 5))

    canvas_frame = create_canvas_frame(root, 400, 300)
    canvas_frame.grid(column=4, row=2, columnspan=3, padx=(10, 10), pady=(5, 5))

    input_frame = create_input_frame(root, 1)
    input_frame.grid(column=0, row=2, padx=(10, 10), pady=(5, 5))

    input_frame = create_input_frame(root, 2)
    input_frame.grid(column=0, row=3, padx=(10, 10), pady=(5, 5))

    input_frame = create_input_frame(root, 3)
    input_frame.grid(column=2, row=2, padx=(10, 10), pady=(5, 5))

    input_frame = create_input_frame(root, 4)
    input_frame.grid(column=2, row=3, padx=(10, 10), pady=(5, 5))



    root.mainloop()


if __name__ == "__main__":
    create_main_window()