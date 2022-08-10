from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser


root = Tk()
root.title("iScribeX")
root.geometry("1900x1000")
root.config(bg="black")

# Set variable for open file name
global open_status_name
open_status_name = False
global selected
selected = False
# Create new file function
def new_file():
	my_text.delete("1.0", END)
	status_bar.config(text="New File")
	root.title("iScribeX | New File")

	global open_status_name
	open_status_name = False

# Open files
def open_file():
	my_text.delete("1.0", END)
	status_bar.config(text="Open File")
	root.title("iScribeX | Open File")

	# Grab filename
	text_file = filedialog.askopenfilename(initialdir="C:/", title = "Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
	
	# Check to see if there is a filename
	if text_file:
		# Make filename global so we can access it later
		global open_status_name
		open_status_name = text_file

	# Update status bars
	name = text_file
	status_bar.config(text=f'{name}        ')
	name = name.replace("C:/","")
	root.title(f'{name} | New File')

	# Open the file
	text_file = open(text_file, 'r')
	stuff = text_file.read()

	# Add file to text box
	my_text.insert(END, stuff)

	# Close the file
	text_file.close()

# Save as
def save_as_file():
	text_file = filedialog.asksaveasfilename(defaultextension=".*",initialdir="C:/", title ="Save File", filetypes= (("Text Files","*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
	if text_file:
		# Update status bars
		name = text_file
		name = name.replace("C:/", "")
		status_bar.config(text=f'Saved : {name}        ')
		root.title(f'{name} | New File')

		# Save the file
		text_file = open(text_file,'w')
		text_file.write(my_text.get(1.0, END))
		# Close the file
		text_file.close()
	


# Save file
def save_file():
	global open_status_name
	if open_status_name:

		# Save the file
		text_file = open(open_status_name,'w')
		text_file.write(my_text.get(1.0, END))
		# Close the file
		text_file.close()
		status_bar.config(text=f'Saved : {open_status_name}        ')
	else:
		save_as_file()

# Cut text
def cut_text(e):
	global selected
	# Check to see if we used keyboard shortcuts
	if e:
		selected = root.clipboard_get()
	else:
		if my_text.selection_get():
			# Grab text from text box
			selected = my_text.selection_get()

			# Delete text from text box
			my_text.delete("sel.first","sel.last")

			# Clear clipboard then append
			root.clipboard_clear()
			root.clipboard_append(selected)
# Copy text
def copy_text(e):
	global selected

	# Check to see if we used keyboard shortcuts
	if e:
		selected = root.clipboard_get()

	if my_text.selection_get():
		# Grab text from text box
		selected = my_text.selection_get()
		# Clear clipboard then append
		root.clipboard_clear()
		root.clipboard_append(selected)

# Paste text
def paste_text(e):
	global selected

	# Check to see if we used keyboard shortcuts
	if e:
		selected = root.clipboard_get()
	else:
		if selected:
			position = my_text.index(INSERT)
			my_text.insert(position, selected)


# Bold

def bold_it():
	# Create font
	bold_font = font.Font(my_text, my_text.cget("font"))
	bold_font.configure(weight="bold")

	# Configure a tag
	my_text.tag_configure("bold", font=bold_font)


	# Define current tags
	current_tags = my_text.tag_names("sel.first")


	if "bold" in current_tags:
		my_text.tag_remove("bold", "sel.first", "sel.last")
	else:
		my_text.tag_add("bold", "sel.first", "sel.last")

# Italics

def italics_it():
	# Create font
	italics_font = font.Font(my_text, my_text.cget("font"))
	italics_font.configure(slant="italic")

	# Configure a tag
	my_text.tag_configure("italic", font=italics_font)


	# Define current tags
	current_tags = my_text.tag_names("sel.first")


	if "italic" in current_tags:
		my_text.tag_remove("italic", "sel.first", "sel.last")
	else:
		my_text.tag_add("italic", "sel.first", "sel.last")


# Change color

def text_color():

	# Pick a color
	my_color = colorchooser.askcolor()[1]
	if my_color:

		# Create font
		color_font = font.Font(my_text, my_text.cget("font"))

		# Configure a tag
		my_text.tag_configure("colored", font=color_font, foreground = my_color)


		# Define current tags
		current_tags = my_text.tag_names("sel.first")


		if "colored" in current_tags:
			my_text.tag_remove("colored", "sel.first", "sel.last")
		else:
			my_text.tag_add("colored", "sel.first", "sel.last")

# Background color
def bg_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(bg=my_color)

# All text color
def all_text_color():
	mycolor = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(fg=my_color)


# Print file
def print_file():
	pass


# Select all text
def select_all(e):
	# Add sel tag to select all text
	my_text.tag_add('sel', '1.0', 'end')


# Clear all text
def clear_all():
	my_text.delete(1.0, END)


title = Label(root, text="Welcome to iScribeX", font=("Halvetica", 24), bg="black", fg="white")
title.pack(pady=20)

# Create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.config(bg="blue")
toolbar_frame.pack(fill=X)

# Logo
logo = Label(root, text="iScribeX", font=("Halvetica", 24, 'bold'), fg="white", bg="black")
logo.place(x=25, y=15)

# Create the main frame
my_frame = Frame(root)
my_frame.place(x=45,y=125)

# Create the scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Horizontal the scrollbar
horizontal_scroll = Scrollbar(my_frame, orient='horizontal')
horizontal_scroll.pack(side=BOTTOM, fill=X)


# Create the text widget
my_text= Text(my_frame, width=150, height=32, font=("Halvetica", 16), selectbackground="blue", selectforeground="black", undo = True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=horizontal_scroll.set)
my_text.pack()

# Configure scrollbar
text_scroll.config(command=my_text.yview)

# Configure horizontal scrollbar
horizontal_scroll.config(command=my_text.xview)


# Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# File menu
file_menu = Menu(my_menu, tearoff=False)

my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command = new_file)
file_menu.add_command(label="Open", command = open_file)
file_menu.add_command(label="Save", command = save_file)
file_menu.add_command(label="Save As", command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print File", command = print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = root.quit)

# Edit menu
edit_menu = Menu(my_menu, tearoff=False)

my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command = lambda:cut_text(False), accelerator="Ctrl+x")
edit_menu.add_command(label="Copy", command = lambda:copy_text(False), accelerator="Ctrl+c")
edit_menu.add_command(label="Paste", command = lambda:paste_text(False), accelerator="Ctrl+v")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command = my_text.edit_undo, accelerator="Ctrl+z")
edit_menu.add_command(label="Redo", command = my_text.edit_redo, accelerator="Ctrl+y")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command = lambda: select_all(True), accelerator="Ctrl+a")
edit_menu.add_command(label="Clear", command = clear_all, accelerator="Ctrl+y")

# Add status bar to bottom of app
status_bar = Label(root, text="Ready        ", fg="white",anchor=E)
status_bar.config(bg="blue")
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# Edit bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

# Select binding
root.bind('<Control-A>', select_all)
root.bind('<Control-a>', select_all)

# Color menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected Text", command = text_color)
color_menu.add_command(label="All Text", command = all_text_color)
color_menu.add_command(label="Background", command = bg_color)

# Buttons
bold_button = Button(toolbar_frame, text="Bold", command = bold_it)
bold_button.grid(row=0, column = 0, sticky=W)

italics_button = Button(toolbar_frame, text="Italics", command = italics_it)
italics_button.grid(row=0, column = 1, sticky=W)

undo_button = Button(toolbar_frame, text="Undo", command = my_text.edit_undo)
undo_button.grid(row=0, column = 2, sticky=W)

redo_button = Button(toolbar_frame, text="Redo", command = my_text.edit_redo)
redo_button.grid(row=0, column = 3, sticky=W)

# Text color
color_text_button = Button(toolbar_frame, text="Font Color", command = text_color)
color_text_button.grid(row=0,column=4,padx=5)

root.mainloop()
