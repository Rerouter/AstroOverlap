from tkinter import Tk, Canvas, Frame, BOTH, filedialog
import tkinter as tk
import HeaderReading as FITS
root = Tk()  # pointing root to Tk() to use it as Tk() in program.
root.withdraw()  # Hides small tkinter window.


def open_folder():
    """
    :return foldername:
    """
    foldername = filedialog.askdirectory(title="Select Folder To Scan")
    if not foldername:
        print("No Folder Selected")
        return 0
    FITS.Directory = foldername
    return foldername


def on_closing():
    window.destroy()
    root.destroy()


def on_list_creation():
    if FITS.Output:
        for record in FITS.Output:
            txt_edit.insert('end', str(record[0]))
            txt_edit.insert('end', '\n')
            for subrecord in record[1]:
                txt_edit.insert('end', '+ ')
                txt_edit.insert('end', str(subrecord[0]))
                txt_edit.insert('end', ' , ')
                txt_edit.insert('end', str(round(subrecord[1], 3)))
                txt_edit.insert('end', '\n')
            txt_edit.insert('end', '\n')

            #txt_edit.insert('end', str.join(str(record[0]), '\n'))
            #txt_edit.insert('end', str.join(str(record[1:]), '\n'))


window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=480, weight=1)
window.columnconfigure(1, minsize=480, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_folder)
btn_save = tk.Button(frm_buttons, text="Process", command=FITS.make_overlap_list)
btn_update = tk.Button(frm_buttons, text="Update", command=on_list_creation)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_update.grid(row=2, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

canvas = Canvas(txt_edit,width=400,height=400,background='white')
canvas.grid(row=0,column=0)
#canvas.create_line(100,100,300,100,200,300,100,100,fill='blue',width=4)




window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()



