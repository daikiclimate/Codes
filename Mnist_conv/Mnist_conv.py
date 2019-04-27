import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
import torch.optim as optim
import torch.nn as nn
import numpy as np
batch_size = 128

class Flatten(nn.Module):
    def forward(self, input):
        return input.view(input.size(0), -1)

#トレインデータ、テストデータのロード
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, ), (0.5, ))])
trainset = torchvision.datasets.MNIST(root='./data', 
                                        train=True,
                                        download=True,
                                        transform=transform)
trainloader = torch.utils.data.DataLoader(trainset,
                                            batch_size=batch_size,
                                            shuffle=True)

testset = torchvision.datasets.MNIST(root='./data', 
                                        train=False, 
                                        download=True, 
                                        transform=transform)
testloader = torch.utils.data.DataLoader(testset, 
                                            batch_size=batch_size,
                                            shuffle=False)

#モデルの定義
model = torch.nn.Sequential(
    nn.Conv2d(1, 8, 5),  # 28 * 28 * 16-> 24 * 24 * 16
    nn.ReLU(),
    nn.MaxPool2d(2), #24 * 24 *16 -> 12 * 12 * 16    
    nn.Conv2d(8, 16,  5), # 12* 12 * 16 -> 8* 8 * 32
    nn.ReLU(),
    nn.Dropout2d(),
    Flatten(),
    nn.Linear(8 * 8 * 16, 128),
    nn.Linear(128, 10)
)

#勾配法
optimizer = optim.SGD(model.parameters(), lr=0.01)
#誤差関数
criterion = nn.CrossEntropyLoss()

training_loss = []

#モデルの学習
model.train()
for i in range(10):
    runnning_loss = 0.0
    for j, data in enumerate(trainloader):
        inputs, teacher_labels = data
        model.zero_grad()
        outputs = model(inputs)    
        
        #lossの計算逆伝搬
        loss = criterion(outputs,teacher_labels)
        loss.backward()
        optimizer.step()
        
        runnning_loss += loss.data.item()
        
        #途中結果の表示
        #バッチサイズに合わせて変更する必要あり
        if j % 100 == 99:
            print("[{:d}, {:d} loss : {:.3f}]".format(i, j+1, runnning_loss/2000))
            runnning_loss = 0.0
    training_loss.append(loss)
      
count_when_correct = 0
total = 0

for data in testloader:
  #テストデータのロード
  test_data, test_labels = data
  
  #テストデータの推論
  outputs = model(test_data)
  _, predicted = torch.max(outputs.data, 1)
  #正答率の算出
  total += test_labels.size(0)
  count_when_correct += (predicted == test_labels).sum()
    
print('正解率：%d / %d => %.1f'% (count_when_correct, total, int(count_when_correct)/int(total)*100 ),"%")
