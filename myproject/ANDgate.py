import torch
import torch.utils
import torch.nn as nn
import torch.nn.functional as F


class AND(nn.Module):
    def __init__(self):
        super(AND,self).__init__()
        self.fc1  = nn.Linear(20,4)
        self.fc2  = nn.Linear(4,20)
    def forward(self,x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return x
    
model = AND


