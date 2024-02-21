import tkinter as tk
from tkinter import messagebox

# Initialize a dictionary to store the decisions
decisions = {}

def ask_question():
    archon_answer = messagebox.askyesno("Question", "Are they an archon?")
    decisions["Are they an archon?"] = "Yes" if archon_answer else "No"
    
    if archon_answer:
        have_them_answer = messagebox.askyesno("Question", "Do you have them already?")
        decisions["Do you have them already?"] = "Yes" if have_them_answer else "No"
        
        if have_them_answer:
            constellation_answer = messagebox.askyesno("Question", "Do you want more constellations?")
            decisions["Do you want more constellations?"] = "Yes" if constellation_answer else "No"
            
            if constellation_answer:
                messagebox.showinfo("Outcome", "Proceed to wishing")
            else:
                messagebox.showinfo("Outcome", "Skip")
        else:
            want_them_answer = messagebox.askyesno("Question", "Do you want them?")
            decisions["Do you want them?"] = "Yes" if want_them_answer else "No"
            
            if want_them_answer:
                messagebox.showinfo("Outcome", "Proceed to wishing")
            else:
                rerun_answer = messagebox.askyesno("Question", "Proceed to Wishing anyway they OP?")
                decisions["Proceed to Wishing anyway they OP?"] = "Yes" if rerun_answer else "No"
                
                if rerun_answer:
                    messagebox.showinfo("Outcome", "Proceed to wishing anyway they OP")
                else:
                    messagebox.showinfo("Outcome", "Skip and wait for rerun")
    else:
        cool_answer = messagebox.askyesno("Question", "Does the character look cool?")
        decisions["Does the character look cool?"] = "Yes" if cool_answer else "No"
        
        if cool_answer:
            want_cool_character_answer = messagebox.askyesno("Question", "Do you want them?")
            decisions["Do you want them? (cool character)"] = "Yes" if want_cool_character_answer else "No"
            
            if want_cool_character_answer:
                messagebox.showinfo("Outcome", "Proceed to wishing")
            else:
                messagebox.showinfo("Outcome", "Skip")
        else:
            strong_answer = messagebox.askyesno("Question", "Is the character strong or OP?")
            decisions["Is the character strong or OP?"] = "Yes" if strong_answer else "No"
            
            if strong_answer:
                play_style_answer = messagebox.askyesno("Question", "Do you like the play style?")
                decisions["Do you like the play style?"] = "Yes" if play_style_answer else "No"
                
                if play_style_answer:
                    messagebox.showinfo("Outcome", "Proceed to wishing")
                else:
                    messagebox.showinfo("Outcome", "Skip")
            else:
                messagebox.showinfo("Outcome", "Skip")

    # Print the decisions at the end of each question sequence
    print(decisions)
    
    # After each decision, call update_decision_tree
    update_decision_tree()

def update_decision_tree():
    # Delete the current text in the widget
    decision_tree.delete(1.0, tk.END)

    # Insert the updated decisions into the widget
    decision_tree.insert(tk.END, "\n".join(f"{question}: {answer}" for question, answer in decisions.items()))

def create_window():
    window = tk.Tk()
    window.title("Interactive Decision Tree")
    
    btn = tk.Button(window, text="Wishing flow chart", command=ask_question, font=('Times New Roman', '20'))  # Adjust the font size here
    btn.pack()
    
    create_decision_tree_window(window)
    
    window.mainloop()

def create_decision_tree_window(master):
    global decision_tree

    decision_tree_window = tk.Toplevel(master)
    decision_tree_window.title("Decision Tree")

    # Create a Text widget to display the decision tree
    decision_tree = tk.Text(decision_tree_window)
    decision_tree.pack()

create_window()