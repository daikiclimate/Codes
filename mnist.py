import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
import torch.optim as optim
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, ), (0.5, ))])
trainset = torchvision.datasets.MNIST(root='./data', 
                                        train=True,
                                        download=True,
                                        transform=transform)
trainloader = torch.utils.data.DataLoader(trainset,
                                            batch_size=64,
                                            shuffle=True)

testset = torchvision.datasets.MNIST(root='./data', 
                                        train=False, 
                                        download=True, 
                                        transform=transform)
testloader = torch.utils.data.DataLoader(testset, 
                                            batch_size=10,
                                            shuffle=False)
D_in, H, D_out  = 28*28, 50, 10
model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(),
    torch.nn.Linear(H, D_out),
)

optimizer = optim.SGD(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

model.train()
for i in range(10):
    runnning_loss = 0.0
    for j, data in enumerate(trainloader):
        train_data, teacher_labels = data
        inputs = train_data.reshape(-1, 28*28)
        model.zero_grad()
        outputs = model(inputs)    
        loss = criterion(outputs,teacher_labels)
        loss.backward()
        optimizer.step()
        
        runnning_loss += loss.data.item()
        
        if j % 2000 == 1999:
            print(i, j+1, runnning_loss/2000)
            runnning_loss = 0.0
