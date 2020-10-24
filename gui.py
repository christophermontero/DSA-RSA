# import all components
# from the tkinter library
import tkinter as tk

# import filedialog module
from tkinter import filedialog

# Import owner classes
import algorithms as alg  # Import all the algorithms to this file
import utils

# Function for opening the
# file explorer root

def browseFiles():
  filename = filedialog.askopenfilename(initialdir="/home/giocom21/Documents",
                                        title="Select a File",
                                        filetypes=(("Text files",
                                                    "*.txt*"),
                                                   ("all files",
                                                    "*.*")))
  file_path.insert(tk.END, filename)

def compute_digest():
  path = file_path.get()
  # Convert file from utf-8 to bytes
  convert = utils.convert(path)
  text_to_bytes = convert.to_bytes()

  # Get hash function value
  label_hash_function = control_variable.get()

  # Compute digest
  _hash = alg.hash(label_hash_function, text_to_bytes)
  digest = _hash.function()

  digest_text.insert(tk.END, digest)

# Create the root root
root = tk.Tk()

# Set root title
root.title('DSA')

canvas = tk.Canvas(root,
                   height=740,
                   width=1360,
                   bg="#0e6655")
canvas.pack()

frame1 = tk.Frame(root, bg="#73c6b6")

frame1.place(relwidth=0.9,
             relheight=0.2,
             relx=0.05,
             rely=0.05)

frame2 = tk.Frame(root, bg="#73c6b6")

frame2.place(relwidth=0.9,
             relheight=0.7,
             relx=0.05,
             rely=0.28)

### Widgets frame 1 ###

# Create a password label
label_password = tk.Label(frame1)
label_password.config(text="Enter your password",
                      fg="black",
                      bg="#73c6b6",
                      pady=8,
                      font=("Times", 14, "italic"))

# Create a password entry
entry_password = tk.Entry(frame1)
entry_password.config(width=60,
                      fg="black",
                      bg="white")

# Create a File Explorer label
label_file_explorer = tk.Label(frame1)
label_file_explorer.config(text="Select a text file",
                           fg="black",
                           bg="#73c6b6",
                           pady=8,
                           font=("Times", 12, "italic"))

# Create a file explorer button
button_explore = tk.Button(frame1,
                           text="Browse Files",
                           command=browseFiles)

file_path = tk.Entry(frame1)

### Widgets frame 2 ###

# Create a select hash function label
label_hash_function = tk.Label(frame2)
label_hash_function.config(text="Select a hash funcion",
                           fg="black",
                           bg="#73c6b6",
                           pady=8,
                           font=("Times", 12, "italic"))
# Create a digest button
button_digest = tk.Button(frame2,
                          text="Compute digest",
                          command=compute_digest)

# Create hash option menu
control_variable = tk.StringVar(frame2)
control_variable.set("SHA224")
OPTION_TUPLE = ("SHA224", "SHA256", "SHA384", "SHA512", "keccak")
optionmenu_hash = tk.OptionMenu(frame2,
                                control_variable,
                                *OPTION_TUPLE)

# Create a text field wiht digest
digest_text = tk.Text(frame2)

# Create encrypt button
button_encrypt = tk.Button(frame2,
                           text="Encrypt RSA")

# Create decrypt button
button_decrypt = tk.Button(frame2,
                           text="Decrypt RSA")

# Create a text field wiht digest encrypted
encrypt_rsa_text = tk.Text(frame2)

# Create a text field wiht digest decripted
decrypt_rsa_text = tk.Text(frame2)

# Widgets is being placed in frame 1
label_password.pack()
entry_password.pack()
label_file_explorer.pack()
button_explore.pack()

# Widgets is being placed in frame 2
label_hash_function.pack()
optionmenu_hash.place(relx=0.62,
                      rely=0.01)
button_digest.pack()
digest_text.place(relwidth=0.95,
                  relheight=0.2,
                  relx=0.025,
                  rely=0.18)
button_encrypt.place(relx=0.025,
                     rely=0.4)
encrypt_rsa_text.place(relwidth=0.95,
                       relheight=0.2,
                       relx=0.025,
                       rely=0.48)
button_decrypt.place(relx=0.025,
                     rely=0.71)
decrypt_rsa_text.place(relwidth=0.95,
                       relheight=0.2,
                       relx=0.025,
                       rely=0.78)

# Let the root wait for any events
root.mainloop()
