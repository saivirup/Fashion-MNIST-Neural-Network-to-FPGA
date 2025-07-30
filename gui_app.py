import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk
from Neural_Network import *
from Neural_Network import Model, fashion_mnist_labels, preprocess_image

# Load the trained model
model = Model.load('fashion_mnist.model')

def predict_from_path(file_path):
    file_path = file_path.strip("{}")  # Remove curly braces if present
    try:
        img_display = Image.open(file_path).resize((150, 150))
        img_tk = ImageTk.PhotoImage(img_display)
        panel.config(image=img_tk)
        panel.image = img_tk

        img_data = preprocess_image(file_path)
        confidences = model.predict(img_data)
        prediction_idx = model.output_layer_activation.predictions(confidences)[0]
        prediction_label = fashion_mnist_labels[prediction_idx]
        result_label.config(text=f"Prediction: {prediction_label}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Main GUI window
root = TkinterDnD.Tk()
root.title("Fashion MNIST Classifier")

panel = tk.Label(root)
panel.pack()

result_label = tk.Label(root, text="Drop an image here")
result_label.pack()

# Bind the drop event
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', lambda e: predict_from_path(e.data))

root.mainloop()
