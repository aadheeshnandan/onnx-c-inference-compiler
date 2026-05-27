import torch
import torch.nn as nn

class TinyMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(4, 8)
        self.fc2 = nn.Linear(8, 8)
        self.fc3 = nn.Linear(8, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = TinyMLP()
model.eval()

dummy_input = torch.randn(1, 4)

torch.onnx.export(
    model,
    dummy_input,
    "models/tiny_mlp.onnx",
    input_names=["input"],
    output_names=["output"],
    opset_version=13,
)
print("Exported models/tiny_mlp.onnx")
