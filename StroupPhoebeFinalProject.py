import tkinter as tk
from tkinter import messagebox
from db import Database
from PIL import ImageTk, Image

db = Database('store.db')

# Main Application/GUI class

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title("Phoebe's Shoe Emporium")
        # Width height and background color
        master.geometry("900x350")
        master.configure(bg='#b3e6ff')
        # Create widgets/grid
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        # Populate initial list
        self.populate_list()

    def create_widgets(self):
        # Widgets for the SKU, it has the position, font information and background color.
        self.sku_text = tk.StringVar()
        self.sku_label = tk.Label(
            self.master, text='SKU', font=('bold', 14), bg='#c5fec4')
        self.sku_label.grid(row=0, column=0, sticky=tk.W)
        self.sku_entry = tk.Entry(self.master, textvariable=self.sku_text, borderwidth=5)
        self.sku_entry.grid(row=0, column=1)

        # Widgets for the STYLE, it has the position, font information and background color.
        self.style_text = tk.StringVar()
        self.style_label = tk.Label(
            self.master, text='STYLE', font=('bold', 14), bg='#c5fec4')
        self.style_label.grid(row=0, column=2, sticky=tk.W)
        self.style_entry = tk.Entry(
            self.master, textvariable=self.style_text, borderwidth=5)
        self.style_entry.grid(row=0, column=3)

        # Widgets for the COLOR, it has the position, font information and background color.
        self.color_text = tk.StringVar()
        self.color_label = tk.Label(
            self.master, text='COLOR', font=('bold', 14), bg='#c5fec4')
        self.color_label.grid(row=1, column=0, sticky=tk.W)
        self.color_entry = tk.Entry(
            self.master, textvariable=self.color_text, borderwidth=5)
        self.color_entry.grid(row=1, column=1)

        # Widgets for the SIZE, it has the position, font information and background color.
        self.size_text = tk.StringVar()
        self.size_label = tk.Label(
            self.master, text='SIZE', font=('bold', 14), bg='#c5fec4')
        self.size_label.grid(row=1, column=2, sticky=tk.W)
        self.size_entry = tk.Entry(self.master, textvariable=self.size_text, borderwidth=5)
        self.size_entry.grid(row=1, column=3)

        # Widgets for the QTY, it has the position, font information and background color.
        self.qty_text = tk.StringVar()
        self.qty_label = tk.Label(
            self.master, text='QTY', font=('bold', 14), bg='#c5fec4')
        self.qty_label.grid(row=0, column=4, sticky=tk.W)
        self.qty_entry = tk.Entry(self.master, textvariable=self.qty_text, borderwidth=5)
        self.qty_entry.grid(row=0, column=5)

        # Widgets for the PRICE, it has the position, font information and background color.
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text='PRICE', font=('bold', 14), bg='#c5fec4')
        self.price_label.grid(row=1, column=4, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text, borderwidth=5)
        self.price_entry.grid(row=1, column=5)

        # Listbox of all the shoes and its information
        self.sku_list = tk.Listbox(self.master, height=8, width=50, border=5)
        self.sku_list.grid(row=3, column=0, columnspan=3,
                             rowspan=6, pady=20, padx=20)
        # Scroll bar for the listbox.
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=3)
        # Set scrollbar to parts
        self.sku_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.sku_list.yview)

        # Binding select option to the list.
        self.sku_list.bind('<<ListboxSelect>>', self.select_item)

        # Buttons for add item, remove item, update item, clear input and exit program. It has font information and location of each buttons.
        self.add_btn = tk.Button(
            self.master, text="Add Item", width=12, command=self.add_item, font=('bold, 12'))
        self.add_btn.grid(row=2, column=0, pady=20)

        self.remove_btn = tk.Button(
            self.master, text="Remove Item", width=12, command=self.remove_item, font=('bold, 12'))
        self.remove_btn.grid(row=2, column=1)

        self.update_btn = tk.Button(
            self.master, text="Update Item", width=12, command=self.update_item, font=('bold, 12'))
        self.update_btn.grid(row=2, column=2)

        self.exit_btn = tk.Button(
            self.master, text="Clear Input", width=12, command=self.clear_text, font=('bold, 12'))
        self.exit_btn.grid(row=2, column=3)

        self.button_quit = tk.Button(self.master, text="Exit Program", width=12, command=root.quit, font=('bold, 12'))
        self.button_quit.grid(row=2, column=4)

        #Buttons for different styles and colors of each shoes. Once you click on the button it would open another window with the pictures of the shoes.

        self.new_window = tk.Button(self.master, text="M7652 OPT", width=12, command=self.new_window, font=('bold, 12'))
        self.new_window.grid(row=3, column=4)

        self.new_window1 = tk.Button(self.master, text="M9160 BLK", width=12, command=self.new_window1, font=('bold, 12'))
        self.new_window1.grid(row=3, column=5)

        self.new_window2 = tk.Button(self.master, text="M9697 NVY", width=12, command=self.new_window2,
                                     font=('bold, 12'))
        self.new_window2.grid(row=4, column=4)

        self.new_window3 = tk.Button(self.master, text="W9696 RED", width=12, command=self.new_window3,
                                     font=('bold, 12'))
        self.new_window3.grid(row=4, column=5)


    #For the new windows with the pictures on each window and style and color information. It also have font and background color information. It also have another button for exit that will close the window.
    def new_window(self):
        global my_img
        top = tk.Toplevel()
        top.geometry("900x550")
        top.title("Shoe Images")
        top.configure(bg='#b3e6ff')
        my_img = ImageTk.PhotoImage(Image.open("M7652.png"))
        my_label = tk.Label(top, image=my_img).pack()
        my_label1 = tk.Label(top,text="M7652 OPT", font=('bold, 20')).pack()
        btn2 = tk.Button(top, text="Close Window", command=top.destroy).pack()

    def new_window1(self):
        global my_img1
        top = tk.Toplevel()
        top.geometry("900x750")
        top.title("Shoe Images")
        top.configure(bg='#b3e6ff')
        my_img1 = ImageTk.PhotoImage(Image.open("M9160.png"))
        my_label = tk.Label(top, image=my_img1).pack()
        my_label1 = tk.Label(top,text="M9160 BLK", font=('bold, 20')).pack()
        btn2 = tk.Button(top, text="Close Window", command=top.destroy).pack()

    def new_window2(self):
        global my_img2
        top = tk.Toplevel()
        top.geometry("900x550")
        top.title("Shoe Images")
        top.configure(bg='#b3e6ff')
        my_img2 = ImageTk.PhotoImage(Image.open("M9697.png"))
        my_label = tk.Label(top, image=my_img2).pack()
        my_label1 = tk.Label(top,text="M9697 NVY", font=('bold, 20')).pack()
        btn2 = tk.Button(top, text="Close Window", command=top.destroy).pack()

    def new_window3(self):
        global my_img3
        top = tk.Toplevel()
        top.geometry("900x550")
        top.title("Shoe Images")
        top.configure(bg='#b3e6ff')
        my_img3 = ImageTk.PhotoImage(Image.open("W9696.png"))
        my_label = tk.Label(top, image=my_img3).pack()
        my_label1 = tk.Label(top,text="W9696 RED", font=('bold, 20')).pack()
        btn2 = tk.Button(top, text="Close Window", command=top.destroy).pack()


    def populate_list(self):
        # Delete items before update. So when you keep pressing it doesnt keep getting (show example by calling this twice)
        self.sku_list.delete(0, tk.END)
        # Loop through records
        for row in db.fetch():
            # Insert into list
            self.sku_list.insert(tk.END, row)

    # Information in adding new item.
    def add_item(self):
        if self.sku_text.get() == '' or self.style_text.get() == '' or self.color_text.get() == '' or self.size_text.get() == '' or self.qty_text.get() == '' or self.price_text.get() == '':
            messagebox.showerror(
                "Required Fields", "Please include all fields")
            return
        print(self.sku_text.get())
        # Insert into DB
        db.insert(self.sku_text.get(), self.style_text.get(),
                  self.color_text.get(), self.size_text.get(),
                  self.qty_text.get(), self.price_text.get())
        # Clear list
        self.sku_list.delete(0, tk.END)
        # Insert into list
        self.sku_list.insert(tk.END, (self.sku_text.get(), self.style_text.get(
        ), self.color_text.get(), self.size_text.get(), self.qty_text.get(), self.price_text.get()))
        self.clear_text()
        self.populate_list()

    # Runs when item is selected
    def select_item(self, event):
        # # Create global selected item to use in other functions
        # global self.selected_item
        try:
            # Get index
            index = self.sku_list.curselection()[0]
            # Get selected item
            self.selected_item = self.sku_list.get(index)
            # print(selected_item) # Print tuple

            # Add text to entries
            self.sku_entry.delete(0, tk.END)
            self.sku_entry.insert(tk.END, self.selected_item[1])
            self.style_entry.delete(0, tk.END)
            self.style_entry.insert(tk.END, self.selected_item[2])
            self.color_entry.delete(0, tk.END)
            self.color_entry.insert(tk.END, self.selected_item[3])
            self.size_entry.delete(0, tk.END)
            self.size_entry.insert(tk.END, self.selected_item[4])
            self.qty_entry.delete(0, tk.END)
            self.qty_entry.insert(tk.END, self.selected_item[5])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(tk.END, self.selected_item[6])

        except IndexError:
            pass

    # Remove item
    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    # Update item
    def update_item(self):
        db.update(self.selected_item[0], self.sku_text.get(
        ), self.style_text.get(), self.color_text.get(), self.size_text.get(), self.qty_text.get(), self.price_text.get())
        self.populate_list()

    # Clear all text fields
    def clear_text(self):
        self.sku_entry.delete(0, tk.END)
        self.style_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.size_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)





root = tk.Tk()
app = Application(master=root)
app.mainloop()