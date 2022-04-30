import torch 
from torch import nn
from torch.utils.data import DataLoader
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

class MotoDataset (torch.utils.data.Dataset):

    def __init__(self,X,y,scale_data=True):
        if not torch.is_tensor(X) and not torch.is_tensor(y):
            if scale_data:
                X=StandardScaler().fit_transform(X)
            self.X=torch.from_numpy(X)
            self.y=torch.from_numpy(y)

    def __len__(self):
        return len(self.X)
    
    def __getitem__(self,i):
        return self.X[i], self.y[i]

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(4,64),
            nn.ReLU(),
            nn.Linear(64,32),
            nn.ReLU(),
            nn.Linear(32,1)
        )
    def forward(self,x):
        return self.layers(x)

if __name__ == '__main__':
    torch.manual_seed(42) #Vector inicialización
    data = pd.read_csv("./data/results.csv")
    y= np.asarray(data['PRICE'])
    x= data.drop(columns=['ID','PRICE'])
    print(x)

    #Dataset
    dataset = MotoDataset(x,y) #Crear dataset
    trainloader = torch.utils.data.DataLoader(dataset, batch_size=10, shuffle=True, num_workers=1) #Preparar dataset (Configurable)

    #Inicializar MLP
    mlp= MLP()

    #Loss function para saber performance del modelo y optimizer (Configurables)
    loss_function = nn.MSELoss()
    optimizer = torch.optim.Adam(mlp.parameters(), lr=1e-4) #Configurables (Parametros y learning rate)

    #Training loop
    for epoch in range(0,5): #Configurable
        print(f'Starting epoch {epoch+1}')
        current_loss = 0.0
        for i, data in enumerate(trainloader, 0):

            inputs,targets = data
            inputs, targets = inputs.float(), targets.float()
            targets = targets.reshape((targets.shape[0],1))

            optimizer.zero_grad()

            outputs = mlp(inputs)

            outputs = mlp(inputs)

            loss = loss_function(outputs,targets)

            loss.backward()

            optimizer.step()

            #Statistics
            current_loss += loss.item()
            if i%10 == 0:
                print('Loss after mini-batch %5d: %.3f' %
                (i+1, current_loss /500))
                current_loss = 0.0
    #Process completed
    print('Training finished')







