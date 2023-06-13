import torch
import torch.nn as nn
import torch.optim as optim
import re


class MathNet(nn.Module):
    def __init__(self):
        super(MathNet, self).__init__()
        self.fc = nn.Linear(2, 1)  

    def forward(self, x):
        x = self.fc(x)
        return x


model = MathNet()


criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)


for epoch in range(1000):

    x = torch.randint(low=0, high=100, size=(100, 2), dtype=torch.float)
    operations = torch.randint(low=0, high=4, size=(100, 1), dtype=torch.float)
    y = torch.zeros((100, 1), dtype=torch.float)
    for i in range(100):
        if operations[i] == 0:
            y[i] = x[i, 0] + x[i, 1]
        elif operations[i] == 1:
            y[i] = x[i, 0] - x[i, 1]
        elif operations[i] == 2:
            y[i] = x[i, 0] * x[i, 1]
        elif operations[i] == 3:
            y[i] = x[i, 0] / x[i, 1]


    output = model(x)


    loss = criterion(output, y)


    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


while True:

    input_str = input("Enter a math problem: ")
    

    operands = re.split(r'[+\-*/]', input_str)
    operator = re.findall(r'[+\-*/]', input_str)[0]
    operand1 = float(operands[0])
    operand2 = float(operands[1])
    

    input_tensor = torch.tensor([[operand1, operand2]], dtype=torch.float)
    

    predicted_output = model(input_tensor)
    

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    else:
        result = "Unknown operator"
    
    
    print("Expected Output:", result)
    print()
