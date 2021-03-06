# import all components
# from the tkinter library
import tkinter as tk

# import filedialog module
from tkinter import filedialog

# Import owner classes
import algorithms  # Import all the algorithms to this file
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
  _hash = algorithms.hash(label_hash_function, text_to_bytes)
  digest = _hash.function()

  digest_text.insert(tk.END, digest)


def sign():
  rsa = algorithms.rsa()
  rsa.generate_key_pair()
  digest_bytes = str.encode(digest_text.get('1.0', tk.END))
  sign = rsa.encrypt_key(digest_bytes)
  encrypt_rsa_text.insert(tk.END, sign.hex())


def validate_sign():
  rsa = algorithms.rsa()
  digest_bytes = str.encode(digest_text.get('1.0', tk.END))
  sign = rsa.encrypt_key(digest_bytes)
  sign = rsa.encrypt_key(digest_bytes)
  validation = rsa.decrypt_key(sign)
  decrypt_rsa_text.insert(tk.END, validation.decode())


def gen_cert():
  # Let's get message
  path = file_path.get()
  file_utf8 = open(path, "r", encoding='utf-8')
  text = file_utf8.read()
  file_utf8.close()

  # Let's get public key
  public_key = open('public.pem', "r", encoding='utf-8')
  public_key_text = public_key.read()
  public_key.close()

  # Let's get private key
  private_key = open('private.pem', "r", encoding='utf-8')
  private_key_text = private_key.read()
  private_key.close()

  # Let's get password salted
  password_salted = algorithms.expanded_key(entry_password.get())
  get_salt = password_salted.salt()
  digest_salted = password_salted.digest()

  cert_info = ("- Certificate name: " + entry_certifcate_name.get() + "\n" +
               "- Name: " + entry_name.get() + "\n" +
               "- Salt: " + get_salt + "\n" +
               "- Password: " + digest_salted + "\n" +
               "- Hash function: " + control_variable.get() + "\n" +
               "- Sign algorithm: RSA" + "\n" +
               "- Private key: " + private_key_text + "\n" +
               "- Public key: " + public_key_text + "\n" +
               "- Sign: " + encrypt_rsa_text.get('1.0', tk.END) + "\n" +
               "- Message: " + text)
  certificate_text.insert(tk.END, cert_info)


# Create the root
root = tk.Tk()

# Set root title
root.title('DSA')

canvas = tk.Canvas(root,
                   height=740,
                   width=1360,
                   bg="#0e6655")
canvas.pack()

frame1 = tk.Frame(root, bg="#73c6b6")

frame1.place(relwidth=0.6,
             relheight=0.2,
             relx=0.05,
             rely=0.05)

frame2 = tk.Frame(root, bg="#73c6b6")

frame2.place(relwidth=0.6,
             relheight=0.7,
             relx=0.05,
             rely=0.28)

frame3 = tk.Frame(root, bg="#73c6b6")

frame3.place(relwidth=0.3,
             relheight=0.93,
             relx=0.67,
             rely=0.05)

### Widgets frame 1 ###

# Create title label
label_title = tk.Label(frame1)
label_title.config(text="Digital Signature Algorithm",
                   fg="black",
                   bg="#73c6b6",
                   pady=8,
                   font=("Times", 24, "italic"))

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
                           text="Sign",
                           command=sign)

# Create a text field wiht digest encrypted
encrypt_rsa_text = tk.Text(frame2)

# Create decrypt button
button_decrypt = tk.Button(frame2,
                           text="Validate sign",
                           command=validate_sign)

# Create a text field wiht digest decrypted
decrypt_rsa_text = tk.Text(frame2)

# Create a University name label
label_university_name = tk.Label(frame2)
label_university_name.config(text="Universidad Distrital Francisco José de Caldas",
                             fg="black",
                             bg="#73c6b6",
                             pady=8,
                             font=("Times", 20, "italic"))
# Create a University name label
label_subject = tk.Label(frame2)
label_subject.config(text="Criptorgrafía y Blockchain",
                     fg="black",
                     bg="#73c6b6",
                     pady=8,
                     font=("Times", 14, "italic"))

### Widgets frame 3 ###

# Create a certifcate label
label_certificate = tk.Label(frame3)
label_certificate.config(text="Certificate",
                         fg="black",
                         bg="#73c6b6",
                         pady=8,
                         font=("Times", 24, "italic"))

# Create a certifcate name label
label_certificate_name = tk.Label(frame3)
label_certificate_name.config(text="Certificate name",
                              fg="black",
                              bg="#73c6b6",
                              pady=8,
                              font=("Times", 12, "italic"))

# Create a certifcate name entry
entry_certifcate_name = tk.Entry(frame3)
entry_certifcate_name.config(fg="black",
                             bg="white")

# Create a name label
label_name = tk.Label(frame3)
label_name.config(text="Name",
                  fg="black",
                  bg="#73c6b6",
                  pady=8,
                  font=("Times", 12, "italic"))

# Create a name entry
entry_name = tk.Entry(frame3)
entry_name.config(fg="black", bg="white")

# Create password label
label_password = tk.Label(frame3)
label_password.config(text="Password",
                      fg="black",
                      bg="#73c6b6",
                      pady=8,
                      font=("Times", 12, "italic"))

# Create a password entry
entry_password = tk.Entry(frame3)
entry_password.config(fg="black", bg="white")

# Create generate certificate button
button_gen_certificate = tk.Button(frame3,
                                   text="Generate certificate",
                                   command=gen_cert)

# Create a text field wiht certificate
certificate_text = tk.Text(frame3)

# Widgets is being placed in frame 1
label_title.pack()
label_file_explorer.pack()
button_explore.pack()

# Widgets is being placed in frame 2
label_hash_function.pack()
optionmenu_hash.place(relx=0.62,
                      rely=0.01)
button_digest.pack()
digest_text.place(relwidth=0.95,
                  relheight=0.09,
                  relx=0.025,
                  rely=0.14)
button_encrypt.place(relx=0.025,
                     rely=0.25)
encrypt_rsa_text.place(relwidth=0.95,
                       relheight=0.15,
                       relx=0.025,
                       rely=0.32)
button_decrypt.place(relx=0.025,
                     rely=0.5)
decrypt_rsa_text.place(relwidth=0.95,
                       relheight=0.09,
                       relx=0.025,
                       rely=0.57)
label_university_name.place(relx=0.1,
                            rely=0.7)
label_subject.place(relx=0.3,
                    rely=0.82)

# Widgets is being placed in frame 3
label_certificate.pack()
label_certificate_name.place(relx=0.05,
                             rely=0.1)
entry_certifcate_name.place(relwidth=0.9,
                            relheight=0.03,
                            relx=0.05,
                            rely=0.15)
label_name.place(relx=0.05,
                 rely=0.18)
entry_name.place(relwidth=0.9,
                 relheight=0.03,
                 relx=0.05,
                 rely=0.23)

label_password.place(relx=0.05,
                     rely=0.26)
entry_password.place(relwidth=0.9,
                     relheight=0.03,
                     relx=0.05,
                     rely=0.31)
button_gen_certificate.place(relx=0.05,
                             rely=0.36)
certificate_text.place(relwidth=0.9,
                       relheight=0.55,
                       relx=0.05,
                       rely=0.41)

# Let the root wait for any events
root.mainloop()
