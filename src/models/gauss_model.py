import torch
from torch import nn
from math import sqrt


class GaussAct(nn.Module):
    def __init__(self, std_dev=0.003):
        super().__init__()
        self.std_dev = torch.Tensor([std_dev])

    def forward(self, x):
        return torch.exp(-torch.pow(x, 2) / (2*torch.pow(self.std_dev,2)))



class GaussLayer(nn.Module):
    """Implements a single SIREN layer.
    Args:
        dim_in (int): Dimension of input.
        dim_out (int): Dimension of output.
        w0 (float):
        c (float): c value from SIREN paper used for weight initialization.
        is_first (bool): Whether this is first layer of model.
        use_bias (bool):
        activation (torch.nn.Module): Activation function. If None, defaults to
            Sine activation.
    """

    def __init__(self, dim_in, dim_out, std_dev=0.003, is_first=False,
                 use_bias=True, activation=None):
        super().__init__()
        self.dim_in = dim_in
        self.is_first = is_first

        self.linear = nn.Linear(dim_in, dim_out, bias=use_bias)

        nn.init.uniform_(self.linear.weight, 0, 1)
        if use_bias:
            nn.init.uniform_(self.linear.bias, 0, 1)

        self.activation = GaussAct(std_dev) if activation is None else activation

    def forward(self, x):
        out = self.linear(x)
        out = self.activation(out)
        return out


class Gauss(nn.Module):
    """SIREN model.
    Args:
        dim_in (int): Dimension of input.
        dim_hidden (int): Dimension of hidden layers.
        dim_out (int): Dimension of output.
        num_layers (int): Number of layers.
        w0 (float): Omega 0 from SIREN paper.
        w0_initial (float): Omega 0 for first layer.
        use_bias (bool):
        final_activation (torch.nn.Module): Activation function.
    """

    def __init__(self, dim_in, dim_hidden, dim_out, num_layers, std_dev = 0.003, use_bias=True, final_activation=None, num_encoding_functions=None):
        super().__init__()
        if num_encoding_functions is not None:
            for n in num_encoding_functions:
                dim_in += n
        print(f"Dim_in: {dim_in}")
        layers = []
        for ind in range(num_layers):
            is_first = ind == 0
            layer_dim_in = dim_in if is_first else dim_hidden

            layers.append(GaussLayer(
                dim_in=layer_dim_in,
                dim_out=dim_hidden,
                std_dev=std_dev,
                use_bias=use_bias,
                is_first=is_first
            ))

        self.net = nn.Sequential(*layers)

        final_activation = nn.Identity() if final_activation is None else final_activation
        self.last_layer = GaussLayer(dim_in=dim_hidden, dim_out=dim_out, std_dev=std_dev,
                                     use_bias=use_bias, activation=final_activation)

    def forward(self, x):
        x = self.net(x)
        return self.last_layer(x)
