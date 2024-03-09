import tkinter as tk
from PIL import ImageTk, Image

class BubbleBox:
    def __init__(self, canvas, x, y, pizza_name, selection_box):
        self.canvas = canvas
        self.pizza_name = pizza_name
        self.selection_box = selection_box
        self.selected_bubble_id = None
        self.selected_bubble = None
        self.prices = [10, 15, 20, 25]  # Prices for each pizza size
        self.create_bubbles(x, y)
        self.create_label(x + 135, y + 70, pizza_name)


    def create_bubbles(self, x, y):
        # Create bubbles for each pizza size
        bubble_sizes = ['Small', 'Medium', 'Large', 'X-Large']
        self.bubbles = []
        for i in range(4):  # Create bubbles for each size
            x_pos = x + 50 + i * 50  # Center of the box
            y_pos = y + 390  # 10 pixels above the bottom of the box
            radius = 10
            bubble = self.canvas.create_oval(x_pos - radius, y_pos - radius, x_pos + radius, y_pos + radius, outline='black', fill='white')
            bubble_size_label = self.canvas.create_text(x_pos, y_pos + 20, text=bubble_sizes[i], anchor=tk.N)
            bubble_price_label = self.canvas.create_text(x_pos, y_pos + 40, text=f"${self.prices[i]}", anchor=tk.N)
            self.bubbles.append((bubble, bubble_size_label, bubble_price_label))
            self.bind_bubble_click(bubble, i + 1)  # Bind click event for each bubble

    def create_label(self, x, y, text):
        self.canvas.create_text(x, y, text=text, anchor=tk.N)

    def create_bubble_labels(self, x, y):
        for i in range(6):
            x_pos = x + 50 + i * 50
            y_pos = y + 100
            bubble_label = self.canvas.create_text(x_pos, y_pos, text=str(i+1), anchor=tk.N, state=tk.HIDDEN)
            self.bubbles.append(bubble_label)

    def bind_bubble_click(self, bubble_id, bubble_num):
        self.canvas.tag_bind(bubble_id, '<Button-1>', lambda event, bubble=bubble_id, bubble_num=bubble_num: self.on_bubble_click(event, bubble, bubble_num))
        
    def on_bubble_click(self, event, bubble_id, bubble_num):
        if self.selected_bubble_id == bubble_id:
            # Deselect bubble if clicked again
            self.canvas.itemconfig(bubble_id, fill='white')
            self.selected_bubble_id = None
            self.selected_bubble = None
            self.selection_box.update_selected_text(self.pizza_name, None)
        else:
            if self.selected_bubble_id is not None:
                self.canvas.itemconfig(self.selected_bubble_id, fill='white')
            self.canvas.itemconfig(bubble_id, fill='blue')
            self.selected_bubble_id = bubble_id
            self.selected_bubble = (self.pizza_name, self.prices[bubble_num - 1])
            self.selection_box.update_selected_text(self.pizza_name, (self.pizza_name, bubble_num))

            
class SelectionBox:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.selection_text_ids = {}
        self.selection_text = ''
        self.create_selection_texts(x, y)

    def create_selection_texts(self, x, y):
        pizza_names = ['Cheese', 'Pepperoni', 'Sausage', 'Meat Lovers', 'BBQ', 'Margherita']
        for pizza_name in pizza_names:  # Update to match the number of pizza types
            pizza_y = y + (pizza_names.index(pizza_name)) * 100
            text_id = self.canvas.create_text(x, pizza_y, text=f'{pizza_name}', font=('Helvetica', 16), anchor=tk.W)
            self.selection_text_ids[pizza_name] = text_id

    def update_selected_text(self, group_num, pizza):
        text_id = self.selection_text_ids[group_num]
        if pizza is None:
            self.canvas.itemconfig(text_id, text=f'')
        else:
            pizza_name, bubble_num = pizza
            size = ['Small', 'Medium', 'Large', 'X-Large'][bubble_num - 1]
            price = [10, 15, 20, 25][bubble_num - 1]  # Assuming prices are based on size
            self.canvas.itemconfig(text_id, text=f'{pizza_name}, {size}, ${price}')
            
def open_second_window():
    second_window = tk.Toplevel()
    second_window.title("Checkout")
    second_window.geometry("1000x667")
    second_window.resizable(False, False)

    # Create a canvas for the background image
    second_canvas = tk.Canvas(second_window, width=1000, height=667)
    second_canvas.pack()

    # Load and display the background image
    second_background_image = Image.open(r'C:\Picture\pizza2.png')
    second_background_photo = ImageTk.PhotoImage(second_background_image)
    second_canvas.create_image(0, 0, anchor=tk.NW, image=second_background_photo)

    # Create a white box with message
    box_width = 800
    box_height = 200
    box_x = (1000 - box_width) / 2
    box_y = (667 - box_height) / 2
    second_canvas.create_rectangle(box_x, box_y, box_x + box_width, box_y + box_height, fill='white')
    
    message = "Thank you for your purchase! Your order will be ready shortly."
    second_canvas.create_text(500, 333, text=message, font=("French Script MT", 32), fill="green")

    second_window.mainloop()

def main():
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("1920x1080")  # Set initial window size
    root.resizable(False, False)
    
    # Create a frame for the canvas
    canvas_frame = tk.Frame(root)
    canvas_frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas for the background image
    canvas = tk.Canvas(canvas_frame)
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # Load and display the background image
    background_image = Image.open(r'C:\Picture\pizza1.png')
    background_photo = ImageTk.PhotoImage(background_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)
    
    # Create a frame for the selection box
    selection_box_frame = tk.Frame(root)
    selection_box_frame.pack()

    selection_box = SelectionBox(canvas, 1410, 130)

    # Center positions for each group
    group_positions = [
        (210, 50),  # Group 1
        (620, 50),  # Group 2
        (1024, 50), # Group 3
        (210, 550),  # Group 4
        (620, 550),  # Group 5
        (1024, 550)  # Group 6
    ]

    # Create bubbles for each group
    pizza_names = ['Cheese', 'Pepperoni', 'Sausage', 'Meat Lovers', 'BBQ', 'Margherita']
    for i, (x, y) in enumerate(group_positions):
        group_num = pizza_names[i]  # Pass pizza names
        x_pos = x
        y_pos = y
        group = BubbleBox(canvas, x_pos, y_pos, group_num, selection_box)

    second_window_button = tk.Button(selection_box_frame, text="Open Checkout", command=open_second_window)
    second_window_button.pack()  # Pack the button in the selection box frame
    
    root.mainloop()
if __name__ == "__main__":
    main()