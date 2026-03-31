import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

class SupplyChainGNN(torch.nn.Module):
    def __init__(self, num_node_features, hidden_channels):
        super(SupplyChainGNN, self).__init__()
        # Initialize graph convolution layers
        self.conv1 = GCNConv(num_node_features, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, hidden_channels)
        # Linear layer for final failure probability prediction
        self.linear = torch.nn.Linear(hidden_channels, 1)

    def forward(self, x, edge_index):
        # x: Node feature matrix (e.g., supplier financial health, lead times)
        # edge_index: Graph connectivity (who supplies whom)
        
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, p=0.5, training=self.training)
        
        x = self.conv2(x, edge_index)
        x = F.relu(x)
        
        # Predict failure risk score per node
        out = torch.sigmoid(self.linear(x))
        return out

def evaluate_supplier_risk(node_features, edge_index):
    """
    Dummy function to instantiate the model and run a forward pass.
    """
    model = SupplyChainGNN(num_node_features=node_features.shape[1], hidden_channels=16)
    model.eval()
    with torch.no_grad():
        risk_scores = model(node_features, edge_index)
    return risk_scores