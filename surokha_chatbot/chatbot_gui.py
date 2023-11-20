import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial

class HealthCareChatBotGUI:
    def __init__(self, master):
        self.master = master
        master.title("HealthCare ChatBot")

        # Create and set up the GUI elements
        self.label = ttk.Label(master, text="Enter the symptom you are experiencing:")
        self.label.grid(row=0, column=0, pady=10)

        self.symptom_entry = ttk.Entry(master)
        self.symptom_entry.grid(row=0, column=1, pady=10)

        self.days_label = ttk.Label(master, text="From how many days?")
        self.days_label.grid(row=1, column=0, pady=10)

        self.days_entry = ttk.Entry(master)
        self.days_entry.grid(row=1, column=1, pady=10)

        self.submit_button = ttk.Button(master, text="Submit", command=self.show_result)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_result(self):
        symptom = self.symptom_entry.get()
        try:
            num_days = int(self.days_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for days.")
            return

        # Call your existing code to get the result
        result = self.get_result(symptom, num_days)

        # Display the result in a message box
        messagebox.showinfo("Result", result)

    def get_result(self, symptom, num_days):
        # Implement the logic to get the result using your existing code
        # Replace the following line with your logic
        result = f"You may have {symptom} and should take precautions."
        return result


def main():
    root = tk.Tk()
    app = HealthCareChatBotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
