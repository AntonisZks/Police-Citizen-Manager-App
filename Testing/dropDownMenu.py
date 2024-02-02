import tkinter as tk


def on_entry_change(event):
    # Get the text from the entry widget
    current_text = entry.get()

    # Clear the previous suggestions
    suggestion_listbox.delete(0, tk.END)

    # Filter and populate the suggestions based on the current text
    if current_text:
        suggestions = [word for word in word_list if word.startswith(current_text)]
        if suggestions:
            for suggestion in suggestions:
                suggestion_listbox.insert(tk.END, suggestion)

            # Calculate the position to place the suggestion menu
            x, y = entry.winfo_rootx(), entry.winfo_rooty() + entry.winfo_height()
            suggestion_listbox.place(x=x, y=y)  # Place menu under the entry
        else:
            suggestion_listbox.place_forget()  # Hide the suggestion menu
    else:
        suggestion_listbox.place_forget()  # Hide the suggestion menu


def on_suggestion_select(event):
    # Get the selected suggestion from the listbox
    selected_suggestion = suggestion_listbox.get(suggestion_listbox.curselection())

    # Update the entry widget with the selected suggestion
    entry.delete(0, tk.END)
    entry.insert(0, selected_suggestion)


# Sample list of words for suggestions
word_list = ["apple", "banana", "cherry", "date", "grape", "kiwi", "lemon", "orange"]

# Create the main tkinter window
root = tk.Tk()
root.title("Word Suggestion App")

# Create and place an Entry widget for text input
entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind("<KeyRelease>", on_entry_change)

# Create a Listbox widget for suggestions
suggestion_listbox = tk.Listbox(root)

# Run the Tkinter main loop
root.mainloop()
