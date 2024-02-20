import tkinter as tk

def move_text():
    canvas.move(text_id, 5, 0)  # Move the text 5 pixels to the right
    canvas.after(50, move_text)  # Call move_text again after 50 milliseconds

root = tk.Tk()
root.title("Left-to-Right Moving Text")

# Create a frame to hold the canvas
frame = tk.Frame(root)
frame.grid(row=0, column=0)

canvas = tk.Canvas(frame, width=400, height=100)
canvas.grid(row=0, column=0)

text_id = canvas.create_text(10, 50, text="Moving Text", anchor="w", font=("Arial", 16))

move_text()  # Start the text animation

root.mainloop()