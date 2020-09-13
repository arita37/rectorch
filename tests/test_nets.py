"""Unit tests for the rectorch.nets module
"""
import os
import sys
import pytest
import torch
sys.path.insert(0, os.path.abspath('..'))

from rectorch.models.nn import NeuralNet, AE_net, VAE_net
from rectorch.models.nn.cfgan import CFGAN_G_net, CFGAN_D_net
from rectorch.models.nn.multvae import MultVAE_net
from rectorch.models.nn.multdae import MultDAE_net
from rectorch.models.nn.recvae import RecVAE_net
from rectorch.models.nn.svae import SVAE_net
from rectorch.models.nn.cvae import CMultVAE_net

def test_NeuralNet():
    """Test the NeuralNet class
    """
    nn = NeuralNet()
    with pytest.raises(NotImplementedError):
        nn.forward()

    with pytest.raises(NotImplementedError):
        nn.init_weights()

    assert nn.get_state() == {}


def test_AE_net():
    """Test the AE_net class
    """
    net = AE_net([1, 2], [2, 1])
    x = torch.FloatTensor([[1, 1], [2, 2]])

    with pytest.raises(NotImplementedError):
        net.encode(x)

    with pytest.raises(NotImplementedError):
        net.decode(x)

    with pytest.raises(NotImplementedError):
        net.forward(x)

    with pytest.raises(NotImplementedError):
        net.init_weights()

    assert hasattr(net, "enc_dims"), "Missing enc_dims attribute"
    assert hasattr(net, "dec_dims"), "Missing dec_dims attribute"

def test_VAE_net():
    """Test the VAE_net class
    """
    net = VAE_net([1, 2], [2, 1])
    x = torch.FloatTensor([[1, 1], [2, 2]])
    y, mu, logvar = net.forward(x)

    assert hasattr(net, "enc_dims"), "Missing enc_dims attribute"
    assert hasattr(net, "dec_dims"), "Missing dec_dims attribute"
    assert isinstance(y, torch.Tensor)
    assert isinstance(mu, torch.Tensor)
    assert isinstance(logvar, torch.Tensor)
    assert y.shape == torch.Size([2, 2])
    assert mu.shape == torch.Size([2, 1])
    assert logvar.shape == torch.Size([2, 1])

'''
def test_CDAE_net():
    """Test the CDAE_net class
    """
    net = CDAE_net(2, 2, 2)
    x = torch.FloatTensor([[1, 1, 1, 1], [2, 2, 3, 3]])
    y = net(x)

    assert hasattr(net, "n_items"), "Missing n_items attribute"
    assert hasattr(net, "n_users"), "Missing n_users attribute"
    assert hasattr(net, "dropout"), "Missing dropout attribute"
    assert hasattr(net, "latent_size"), "Missing latent_size attribute"
    assert hasattr(net, "sigmoid_hidden"), "Missing sigmoid_hidden attribute"
    assert hasattr(net, "sigmoid_out"), "Missing sigmoid_out attribute"
    assert isinstance(net.dropout_rate, float), "dropout must be a float"
    assert net.dropout.p == .5, "dropout probability must be equal to .5"
    assert not net.sigmoid_hidden
    assert not net.sigmoid_out
    assert isinstance(y, torch.FloatTensor), "y should be a torch.FloatTensor"
    assert y.shape == torch.Size([2, 2])
'''

def test_MultiDAE_net():
    """Test the MultiDAE_net class
    """
    net = MultDAE_net([1, 2], [2, 1], .1)
    x = torch.FloatTensor([[1, 1], [2, 2]])
    y = net(x)

    assert hasattr(net, "enc_dims"), "Missing enc_dims attribute"
    assert hasattr(net, "dec_dims"), "Missing dec_dims attribute"
    assert hasattr(net, "dropout_rate"), "Missing dropout attribute"
    assert hasattr(net, "dec_layers"), "Missing dec_layers attribute"
    assert hasattr(net, "enc_layers"), "Missing end_layers attribute"
    assert isinstance(net.dropout_rate, float), "dropout must be a float"
    assert net.dropout_rate == .1, "dropout probability must be equal to .1"
    assert isinstance(y, torch.FloatTensor), "y should be a torch.FloatTensor"
    assert y.shape == x.shape, "The shape of x and y should be the same"


def test_MultiVAE_net():
    """Test the MultiVAE_net class
    """
    net = MultVAE_net([1, 2], [2, 1], .1)
    x = torch.FloatTensor([[1, 1], [2, 2]])
    torch.manual_seed(98765)
    mu, logvar = net.encode(x)
    torch.manual_seed(98765)
    y, mu2, logvar2 = net(x)

    assert hasattr(net, "enc_dims"), "Missing enc_dims attribute"
    assert hasattr(net, "dec_dims"), "Missing dec_dims attribute"
    assert hasattr(net, "dropout_rate"), "Missing dropout attribute"
    assert hasattr(net, "dec_layers"), "Missing dec_layers attribute"
    assert hasattr(net, "enc_layers"), "Missing end_layers attribute"
    assert isinstance(net.dropout_rate, float), "dropout must be a float"
    assert net.dropout_rate == .1, "dropout probability must be equal to .1"
    assert isinstance(y, torch.FloatTensor), "y should be a torch.FloatTensor"
    assert isinstance(mu, torch.FloatTensor), "mu should be a torch.FloatTensor"
    assert isinstance(logvar, torch.FloatTensor), "logvar should be a torch.FloatTensor"
    assert isinstance(mu2, torch.FloatTensor), "mu2 should be a torch.FloatTensor"
    assert isinstance(logvar2, torch.FloatTensor), "logvar2 should be a torch.FloatTensor"
    assert mu.equal(mu2), "mu and mu2 should be equal"
    assert logvar.equal(logvar2), "logvar and logvar2 should be equal"
    assert y.shape == x.shape, "The shape of x and y should be the same"


def test_CMultiVAE_net():
    """Test the CMultiVAE_net class
    """
    net = CMultVAE_net(1, [1, 2], [2, 1], .1)
    x = torch.FloatTensor([[1, 1, 1], [2, 2, 0]])
    torch.manual_seed(98765)
    mu, logvar = net.encode(x)
    torch.manual_seed(98765)
    y, mu2, logvar2 = net(x)

    assert hasattr(net, "enc_dims"), "Missing enc_dims attribute"
    assert hasattr(net, "dec_dims"), "Missing dec_dims attribute"
    assert hasattr(net, "dropout_rate"), "Missing dropout attribute"
    assert hasattr(net, "dec_layers"), "Missing dec_layers attribute"
    assert hasattr(net, "enc_layers"), "Missing end_layers attribute"
    assert isinstance(net.dropout_rate, float), "dropout must be a float"
    assert net.dropout_rate == .1, "dropout probability must be equal to .1"
    assert isinstance(y, torch.FloatTensor), "y should be a torch.FloatTensor"
    assert isinstance(mu, torch.FloatTensor), "mu should be a torch.FloatTensor"
    assert isinstance(logvar, torch.FloatTensor), "logvar should be a torch.FloatTensor"
    assert isinstance(mu2, torch.FloatTensor), "mu2 should be a torch.FloatTensor"
    assert isinstance(logvar2, torch.FloatTensor), "logvar2 should be a torch.FloatTensor"
    assert mu.equal(mu2), "mu and mu2 should be equal"
    assert logvar.equal(logvar2), "logvar and logvar2 should be equal"
    assert y.shape == torch.Size([2, 2]), "The shape of y should be torch.Size([2, 2])"


def test_CFGAN_G_net():
    """Test the CFGAN_G_net class
    """
    net = CFGAN_G_net([2, 3, 4])
    x = torch.FloatTensor([[1, 1], [2, 2]])
    y = net(x)

    assert hasattr(net, "latent_dim"), "Missing latent_dim attribute"
    assert hasattr(net, "input_dim"), "Missing input_dim attribute"
    assert hasattr(net, "layers_dim"), "Missing layers_dim attribute"
    assert net.latent_dim == 2, "latent_dim should be 2"
    assert net.input_dim == 4, "input_dim should be 4"
    assert net.layers_dim == [2, 3, 4], "layers_dim should be [2, 3, 4]"
    assert y.shape == torch.Size([2, 4]), "The shape of y should be torch.Size([2, 4])"


def test_CFGAN_D_net():
    """Test the CFGAN_D_net class
    """
    net = CFGAN_D_net([4, 3, 1])
    x = torch.FloatTensor([[1, 1], [2, 2]])
    y = net(x, x)

    assert hasattr(net, "input_dim"), "Missing input_dim attribute"
    assert hasattr(net, "layers_dim"), "Missing layers_dim attribute"
    assert net.input_dim == 4, "input_dim should be 4"
    assert net.layers_dim == [4, 3, 1], "layers_dim should be [4, 3, 1]"
    assert y.shape == torch.Size([2, 1]), "The shape of y should be torch.Size([2, 1])"

def test_SVAE_net():
    """Test the SVAE_net class
    """
    total_items = 3
    net = SVAE_net(n_items=total_items,
                   embed_size=2,
                   rnn_size=2,
                   dec_dims=[2, total_items],
                   enc_dims=[2, 2])
    x = torch.LongTensor([[0, 2]])
    torch.manual_seed(98765)
    y, mu, logvar = net(x)

    assert hasattr(net, "enc_dims"), "Missing enc_dims attribute"
    assert hasattr(net, "dec_dims"), "Missing dec_dims attribute"
    assert hasattr(net, "dec_layers"), "Missing dec_layers attribute"
    assert hasattr(net, "enc_layers"), "Missing end_layers attribute"
    assert hasattr(net, "n_items"), "Missing n_items attribute"
    assert hasattr(net, "embed_size"), "Missing embed_size attribute"
    assert hasattr(net, "rnn_size"), "Missing rnn_size attribute"
    assert hasattr(net, "item_embed"), "Missing item_embed attribute"
    assert hasattr(net, "gru"), "Missing gru attribute"

    assert isinstance(net.gru, torch.nn.GRU), "dropout must be a torch.nn.GRU"
    assert net.n_items == total_items, "n_items should be equal to %d" %total_items
    assert net.embed_size == 2, "embed_size should be 2"
    assert net.rnn_size == 2, "rnn_size should be 2"
    assert isinstance(y, torch.FloatTensor), "y should be a torch.FloatTensor"
    assert isinstance(mu, torch.FloatTensor), "mu should be a torch.FloatTensor"
    assert isinstance(logvar, torch.FloatTensor), "logvar should be a torch.FloatTensor"

def test_RecVAE_net():
    """Test the RecVAE_net class
    """
    net = RecVAE_net(2, 4, 2)
    x = torch.FloatTensor([[1, 1], [2, 2]])
    torch.manual_seed(98765)
    y, z, mu, logvar = net(x)

    assert hasattr(net, "input_dim"), "Missing input_dim attribute"
    assert hasattr(net, "hidden_dim"), "Missing hidden_dim attribute"
    assert hasattr(net, "latent_dim"), "Missing latent_dim attribute"
    assert hasattr(net, "enc_num_hidden"), "Missing enc_num_hidden attribute"
    assert hasattr(net, "prior_mixture_weights"), "Missing prior_mixture_weights attribute"
    assert isinstance(y, torch.FloatTensor), "y should be a torch.FloatTensor"
    assert isinstance(z, torch.FloatTensor), "z should be a torch.FloatTensor"
    assert isinstance(mu, torch.FloatTensor), "mu should be a torch.FloatTensor"
    assert isinstance(logvar, torch.FloatTensor), "logvar should be a torch.FloatTensor"
    assert y.shape == x.shape, "The shape of x and y should be the same"
    state = net.get_state()
    assert state['params']['hidden_dim'] == 4
    assert state['params']['latent_dim'] == 2
    net2 = RecVAE_net.from_state(state)
    assert net2.input_dim == net.input_dim
    assert net2.hidden_dim == net.hidden_dim
    assert net2.latent_dim == net.latent_dim
