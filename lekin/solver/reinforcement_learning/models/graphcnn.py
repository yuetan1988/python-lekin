import torch
import torch.nn as nn
import torch.nn.functional as F


class MLP(nn.Module):
    def __init__(self, num_layers, input_dim, hidden_dim, output_dim):
        super().__init__()

    def forward(self, x):
        return


class GraphCNN(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, graph_pool, adj):
        return
