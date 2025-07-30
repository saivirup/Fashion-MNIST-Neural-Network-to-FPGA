# Fashion-MNIST Neural Network → FPGA Deployment

This project started as a way to really understand how neural networks work under the hood — no frameworks, no magic functions — just raw Python and NumPy.  
The goal? Train a classifier on the [Fashion-MNIST dataset](https://github.com/zalandoresearch/fashion-mnist) and then take it all the way to an FPGA for real-time inference.

Why? Because building a network from scratch forces you to understand every part of the process: forward passes, backpropagation, weight updates, and all the little details in between.  
And pushing it to hardware means thinking about things like **weight quantization**, **resource usage**, and **latency** — the stuff that actually matters when you want to run models in the real world.

---

## What It Does
- Implements a fully connected neural network from scratch (Python + NumPy)
- ReLU activations, Softmax output, Dropout, and L2 regularization
- Mini-batch gradient descent with adjustable learning rate
- Trains on Fashion-MNIST with 90%+ test accuracy
- **Next step:** Quantize weights and deploy to FPGA via a custom Verilog inference engine

---

## Repo Structure
```
fashion-mnist-neural-network-fpga/
├── src/            # Python source code
├── notebooks/      # Training and exploration notebooks
├── results/        # Accuracy curves, confusion matrix, etc.
├── requirements.txt
└── README.md
```

---

## Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/<your-username>/fashion-mnist-neural-network-fpga.git
cd fashion-mnist-neural-network-fpga
pip install -r requirements.txt
```

---

## Training
Run the training script:
```bash
python src/train.py
```
You can tweak parameters like learning rate, batch size, or number of hidden units directly in the script.

---

## Results (Python Implementation)
| Metric   | Value |
|----------|-------|
| Accuracy | 90%+  |
| Loss     | ~0.35 |

Example accuracy curve:  
![Accuracy Curve](results/accuracy.png)

---

## FPGA Deployment Plan
1. **Weight Quantization** – Convert trained weights to fixed-point representation.
2. **Modular Verilog Inference Engine** – ALU-style computation units for matrix ops.
3. **Deployment & Testing** – Run inference on FPGA, measure latency, and compare to CPU runtime.

---

## License
MIT License – see [LICENSE](LICENSE) for details.

---

## Why This Exists
Honestly, I just wanted to bridge the gap between *"I trained a neural net in Python"* and *"I got it running on actual silicon"*.  
It’s one thing to tweak layers in code, it’s another to make it work under the timing and resource constraints of real hardware.
