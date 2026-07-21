## Tensor

1. What is a tensor?

A tensor is a multi-dimensional data structure used by PyTorch. It is similar to a NumPy array, but it can run on GPU and can be tracked by autograd for gradient computation.

2. What do shape, dtype, and device mean?

`shape` describes the dimensions of a tensor.  
`dtype` describes the data type stored in the tensor, such as `torch.float32` or `torch.int64`.  
`device` describes where the tensor is stored, such as CPU or GPU.

3. Why do we reshape x to [100, 1]?

We reshape `x` to `[100, 1]` because PyTorch models usually expect input data in the format `[num_samples, num_features]`. Here, we have 100 samples and each sample has 1 feature.

## Autograd

1. What does requires_grad=True mean?

`requires_grad=True` tells PyTorch to track operations on this tensor so that gradients can be computed during backpropagation.

2. What does backward() do?

`backward()` performs backpropagation. It applies the chain rule through the computation graph and computes gradients of the final output, usually the loss, with respect to tensors that require gradients.

3. Where is the gradient stored?

The gradient is stored in the `.grad` attribute of leaf tensors that have `requires_grad=True`.

4. Why do gradients accumulate?

PyTorch accumulates gradients by default because this allows gradients from multiple backward passes or mini-batches to be added together. Therefore, we need to clear gradients before each update, otherwise old gradients will affect the new update.

## Manual Linear Regression

1. What are w and b?

`w` is the weight or slope of the linear model, and `b` is the bias or intercept. Together they define the prediction: `y_pred = w * x + b`.

2. What is loss.item()?

`loss` is a PyTorch tensor. `loss.item()` extracts its value as a regular Python number, which is useful for printing, logging, and plotting.

3. Why do we use torch.no_grad() when updating parameters?

We use `torch.no_grad()` because parameter updates should not be tracked by autograd. Updating parameters is part of the optimization process, not part of the forward computation graph.

4. Why do we call w.grad.zero_() and b.grad.zero_()?

We call `zero_()` to clear the gradients after each update. If we do not clear them, PyTorch will accumulate gradients from previous backward passes, which can make the parameter updates incorrect.

## Optimizer

1. What does optimizer.zero_grad() do?

`optimizer.zero_grad()` clears the gradients of all parameters managed by the optimizer before the next backward pass.

2. What does optimizer.step() do?

`optimizer.step()` updates the parameters using their gradients and the optimization rule, such as stochastic gradient descent.

3. How is optimizer similar to manual update?

The optimizer performs the same basic idea as manual gradient descent. In manual update, we write `w = w - learning_rate * w.grad`. With an optimizer, `optimizer.step()` performs this update automatically for all parameters.