import ttkbootstrap as tkb
from tkinter import ttk


def main():
    # Set stylization for root
    style = tkb.Style("cyborg")
    root = style.master
    root.title("MoreStash.py")
    root.iconbitmap('Assets/MS.ico')
    root.geometry('800x500')
    root.minsize(1000, 500)  # Set a minimum size for the window

    # Define and pack the left frame
    left_frame = ttk.Frame(root, padding="10")
    left_frame.pack(side='left', fill='both', expand=True)

    # Now, add widgets to the left_frame as before
    progress_bar = ttk.Progressbar(left_frame, mode='determinate', length=200)
    progress_bar.grid(row=0, column=0, columnspan=2, pady=(0, 10))  # Spanning 2 columns
    progress_bar['value'] = 50

    info_labels_active_tabs = ttk.Frame(left_frame)
    info_labels_active_tabs.grid(row=1, column=0, columnspan=2)  # Container frame for labels

    for i in range(8):
        ttk.Label(info_labels_active_tabs, text=f"Label {i+1}").grid(row=i//2, column=i%2, padx=5, pady=2)

    # Place the Active Tabs header and buttons
    ttk.Label(left_frame, text="Active Tabs", font=('TkDefaultFont', 10, 'bold')).grid(row=2, column=0, columnspan=2)

    tabs_frame = ttk.Frame(left_frame)
    tabs_frame.grid(row=3, column=0, columnspan=2)  # Container frame for tab buttons

    for i in range(1, 9):
        ttk.Button(tabs_frame, text=f"Tab{i}").grid(row=(i-1)//4, column=(i-1)%4, padx=5, pady=2, sticky='ew')

    left_frame.columnconfigure(0, weight=1)  # Make the left frame responsive
    left_frame.columnconfigure(1, weight=1)  # Adjust as needed for responsiveness


    # Frame for the middle section
    middle_frame = ttk.Frame(root, padding="10")
    middle_frame.pack(side='left', fill='both', expand=True)

    # Actions column in the middle frame
    ttk.Label(middle_frame, text="Actions", font=('TkDefaultFont', 10, 'bold')).pack(pady=(0, 5))
    ttk.Button(middle_frame, text="<- Export").pack(fill='x', pady=2)
    ttk.Button(middle_frame, text="Swap").pack(fill='x', pady=2)

    # Right frame setup begins
    # Right frame setup changes
    right_frame = ttk.Frame(root, padding="10")
    right_frame.pack(side='left', fill='both', expand=True)

    # Scrollable area setup
    canvas = tkb.Canvas(right_frame)
    scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    ttk.Label(right_frame, text="External Tabs", font=('TkDefaultFont', 10, 'bold')).pack(pady=(0, 5))
    buttons = [ttk.Button(scrollable_frame, text=f"Button {i}") for i in range(1, 501)]
    for button in buttons:
        button.pack(fill='x', expand=True)

    # Pack scrollbar and canvas
    scrollbar.pack(side='right', fill='y')
    canvas.pack(side='left', fill='both', expand=True)

    # Bind the event to adjust the layout of buttons and canvas scrollregion
    right_frame.bind("<Configure>", lambda event: adjust_button_layout(canvas, scrollable_frame, scrollbar))

    # Adjustments for the 2nd information display
    info_labels_frame_right = ttk.Frame(right_frame, padding="10")
    info_labels_frame_right.grid(row=1, column=0, columnspan=2)
    for i in range(8):
        ttk.Label(info_labels_frame_right, text=f"Label {i+1}").grid(row=i//2, column=i%2, padx=5, pady=2)


    # Make sure all frames are set to expand and fill as the window resizes
    root.columnconfigure(0, weight=1)
    left_frame.columnconfigure(1, weight=1)
    right_frame.columnconfigure(0, weight=1)
    middle_frame.columnconfigure(0, weight=1)

    root.mainloop()

def adjust_button_layout(canvas, frame, scrollbar):
    canvas.update_idletasks()
    bbox = canvas.bbox(tkb.ALL)
    canvas.config(scrollregion=bbox, yscrollcommand=scrollbar.set)
    scrollbar.config(command=canvas.yview)
    # Adjust the frame width to fit the canvas
    frame_width = bbox[2] - bbox[0]
    canvas.itemconfig(1, width=frame_width)


if __name__ == "__main__":
    main()
