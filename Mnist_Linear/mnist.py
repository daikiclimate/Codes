import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
import torch.optim as optim
import torch.nn as nn

#トレインデータ、テストデータのロード
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
                                            batch_size=64,
                                            shuffle=False)
#ハイパーパラメータ
D_in, H, D_out  = 28*28, 50, 10

#モデルの定義
model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(),
    torch.nn.Linear(H, D_out),
)

#勾配法
optimizer = optim.SGD(model.parameters(), lr=0.01)
#誤差関数
criterion = nn.CrossEntropyLoss()

#モデルの学習
model.train()
for i in range(10):
    runnning_loss = 0.0
    for j, data in enumerate(trainloader):
        train_data, teacher_labels = data
        inputs = train_data.reshape(-1, 28*28)
        model.zero_grad()
        outputs = model(inputs)    
        
        #lossの計算逆伝搬
        loss = criterion(outputs,teacher_labels)
        loss.backward()
        optimizer.step()
        
        runnning_loss += loss.data.item()
        
        #途中結果の表示
        #バッチサイズに合わせて変更する必要あり
        if j % 500 == 499:
            print(i, j+1, runnning_loss/2000)
            runnning_loss = 0.0
           
count_when_correct = 0
total = 0

for data in testloader:
  #テストデータのロード
  test_data, test_labels = data
  
  #テストデータの推論
  test_data = test_data.reshape(-1, 28*28)
  outputs = model(test_data)
  _, predicted = torch.max(outputs.data, 1)
  #正答率の算出
  total += test_labels.size(0)
  count_when_correct += (predicted == test_labels).sum()
    
print('正解率：%d / %d => %.1f'% (count_when_correct, total, int(count_when_correct)/int(total)*100 ),"%")

