import sys
import pytest

import torch
from upfirdn2d import upfirdn2d

def test_upfirdn2d(request):
    x_ref = upfirdn2d(
        torch.ones((3,3,5,5)),
        torch.ones((3,3)),
    )
    assert x_ref.shape == (3,3,3,3)
    assert (x_ref == 9).all()

    x_cuda = upfirdn2d(
        torch.ones((3,3,5,5)).cuda(),
        torch.ones((3,3)).cuda(),
    )
    assert x_cuda.shape == (3,3,3,3)
    assert (x_cuda == 9).all()