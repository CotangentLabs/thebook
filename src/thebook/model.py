"""The transformer (Chapters 6-9): blocks, residual stream, LM head.

Stubs for now — assembled over Part III.
"""

from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import Tensor


@dataclass
class GPTConfig:
    vocab_size: int = 50_304
    n_layer: int = 12
    n_head: int = 12
    d_model: int = 768
    block_size: int = 1024


class GPT(torch.nn.Module):
    def __init__(self, config: GPTConfig) -> None:
        super().__init__()
        self.config = config
        raise NotImplementedError

    def forward(self, idx: Tensor, targets: Tensor | None = None):
        """Return logits, and cross-entropy loss when `targets` is given."""
        raise NotImplementedError
