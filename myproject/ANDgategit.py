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
    
model = AND()

print("There is no need to panic my dear citizens")

print("OFC there is a better way to write code,but I am not yet too good at this.")




print("This is only true in the second branch called testing_new_branch.")