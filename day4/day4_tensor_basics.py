# day4_tensor_basics.py
import numpy as np
import torch
def one_dimensional_tensor_creation():
    onedimensionaltensor = torch.tensor([1,2,3])
    print(onedimensionaltensor)         # simply pass the variable name
    print(onedimensionaltensor.shape)   # onedimensionaltensor.shape is an attribute, not a method
    print(onedimensionaltensor.dtype)
    print(onedimensionaltensor.device)  # "Device" tells you where the tensor is physically stored in the computers's hardware

def two_dimensional_tensor_creation():
    twodimensionaltensor = torch.tensor([[1,2],[3,4]])
    print(twodimensionaltensor)
    print(twodimensionaltensor.shape)
    print(twodimensionaltensor.dtype)
    print(twodimensionaltensor.device)

def float_tensor_creation():
    floattensor = torch.tensor([1.2,2.4,3.7],dtype=torch.float)
    print(floattensor)
    print(floattensor.shape)
    print(floattensor.dtype)
    print(floattensor.device)     

# special tensors
def special_tensors_creation():
    zeros = torch.zeros(3,4)
    ones = torch.ones(2,3)
    randn = torch.randn(5)
    array_range = torch.arange(10)
    evenly_spaced = torch.linspace(0,10,100)
    print(zeros)
    print(ones)
    print(randn)
    print(array_range)
    print(evenly_spaced)

# tensor operations
def tensor_operations():
    tensor1 = torch.tensor([1,2,3])
    tensor2 = torch.tensor([3,4,7],dtype=torch.float32)
    tensor3 = torch.tensor([[1],[2],[3]])
    tensor4 = torch.tensor([[1,2],[3,4]])
    plus = torch.add(tensor1,tensor2) # "tensor1 + tensor2" will generate the same result
    print(plus)
    multiply = torch.multiply(tensor1,tensor2)  # "tensor1 * tensor2" will generate the same result
    print(multiply)
    square = torch.square(tensor1)
    print(square)
    mean = torch.mean(tensor2)
    print(mean)
    sum = torch.sum(tensor4)
    print(sum)
    matmul = torch.matmul(tensor1,tensor3)  # "tensor1 @ tensor3" will generate the same result
    print(matmul)

def conversion():
    NumpyArray = np.array([1,2,3,4])
    NumpyToTensor = torch.from_numpy(NumpyArray)
    TensorToBeConverted = torch.tensor([2,3,4,5])
    TensorToNumpy = TensorToBeConverted.numpy()
    print(NumpyToTensor)
    print(TensorToNumpy)

def shape_practice():
    x = torch.linspace(0,10,100)
    reshaped1 = torch.reshape(x,[100,1])
    reshaped2 = x.view([100,1])
    print(x)
    print(reshaped1)
    print(reshaped2)

if __name__ == "__main__":
    one_dimensional_tensor_creation()
    two_dimensional_tensor_creation()
    float_tensor_creation()
    special_tensors_creation()
    tensor_operations()
    conversion()
    shape_practice()