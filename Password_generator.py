import tkinter as tk
import random
import string

def generate_password():
    length = length_entry.get()
    length = int(length) if length.isdigit() else 8
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def accept_password():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        message = f"Username: {username}\nPassword: {password}"
        messagebox.showinfo("Accepted", message)
    else:
        messagebox.showwarning("Incomplete", "Please enter both username and password.")

def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def main():
    global username_entry, length_entry, password_entry

    root = tk.Tk()
    root.title("Password Generator")

    # Create and configure the label for username
    username_label = tk.Label(root, text="Enter User Name:")
    username_label.pack(pady=10)

    # Create and configure the entry field for username
    username_entry = tk.Entry(root, width=30)
    username_entry.pack()

    # Create and configure the label for password length
    length_label = tk.Label(root, text="Enter Length of Password:")
    length_label.pack(pady=10)

    # Create and configure the entry field for password length
    length_entry = tk.Entry(root, width=10)
    length_entry.pack()

    # Create and configure the button to generate password
    generate_button = tk.Button(root, text="Generate Password", command=generate_password)
    generate_button.pack(pady=10)

    # Create and configure the label for generated password
    password_label = tk.Label(root, text="Generated Password:")
    password_label.pack()

    # Create and configure the entry field to display password
    password_entry = tk.Entry(root, width=30)
    password_entry.pack()

    # Create and configure the accept button
    accept_button = tk.Button(root, text="Accept", command=accept_password)
    accept_button.pack(pady=10)

    # Create and configure the reset button
    reset_button = tk.Button(root, text="Reset", command=reset_fields)
    reset_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
