# day4_autograd_basics.py
import torch
def single_variable_differentiation():
    w = torch.tensor(3.0,requires_grad = True) # create a tensor that requires gradient tracking (default requires_grad=False).
    print(w)
    print(w.requires_grad)
    y = w ** 2
    print(y.grad_fn)
    print(y.grad_fn.next_functions)
    y.backward()
    print(w.grad)

def double_variables_differentiation():
    w = torch.tensor(1.0,requires_grad = True)
    b = torch.tensor(0.0,requires_grad = True)
    x = 2.0
    y = 7.0
    loss = (w * x + b - y) ** 2
    loss.backward()
    print(w.grad)
    print(b.grad)

def gradient_accumulation_experiment():
    w = torch.tensor(1.0,requires_grad = True)
    b = torch.tensor(0.0,requires_grad = True)
    x = 2.0
    y = 7.0
    loss = (w * x + b - y) ** 2
    loss.backward()
    print("After First Backward:",w.grad,b.grad)
    loss = (w * x + b - y) ** 2
    loss.backward()
    print("After Second Backward:",w.grad,b.grad)
    # PyTorch accumulates gradients by default, so you need to clear them before each update.
    
if __name__ == "__main__":
    single_variable_differentiation()
    double_variables_differentiation()
    gradient_accumulation_experiment()