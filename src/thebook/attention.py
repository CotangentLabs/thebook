"""Attention (Chapters 4-5): self-attention as a graph/set operation.

Static listings in the text quote from here. Stubs for now.
"""

from __future__ import annotations

import torch
from torch import Tensor


def scaled_dot_product_attention(
    q: Tensor, k: Tensor, v: Tensor, *, causal: bool = True
) -> Tensor:
    """softmax(q k^T / sqrt(d_k)) v, optionally causally masked."""
    raise NotImplementedError


class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model: int, n_heads: int) -> None:
        super().__init__()
        raise NotImplementedError

    def forward(self, x: Tensor) -> Tensor:
        raise NotImplementedError
