import torch

class VeryTinyNerfModel(torch.nn.Module):
  r"""Define a "very tiny" NeRF model comprising three fully connected layers.
  """

  def __init__(self, filter_size=256, num_encoding_functions=6, num_hidden_layers=8):
    super(VeryTinyNerfModel, self).__init__()
    n_input_dims = 3
    # Input layer (default: 39 -> 256)
    input_size = n_input_dims + n_input_dims * 2 * num_encoding_functions
    self.input_layer = torch.nn.Linear(
        input_size, filter_size)
    # Hidden layers
    self.hidden_layers = []
    for i in range(num_hidden_layers):
      # if i == 2:
        # self.hidden_layers.append(torch.nn.Linear(filter_size + input_size, filter_size))
      # else:
        self.hidden_layers.append(torch.nn.Linear(filter_size, filter_size))
    # Output layer
    self.output_layer = torch.nn.Linear(filter_size, 3)
    # Short hand for torch.nn.functional.relu
    self.relu = torch.nn.functional.relu

  def forward(self, x):
    # input_x = x
    x = self.relu(self.input_layer(x))
    for i, hl in enumerate(self.hidden_layers):
      # if i == 2:
        # skip connection
        # x = torch.cat((x, input_x), 1)
      x = self.relu(hl(x))
    # Sigmoid on the output layer b/c RGB is 0-1
    x = torch.sigmoid(self.output_layer(x))
    return x