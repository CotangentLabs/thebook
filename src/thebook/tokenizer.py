"""Tokenization (Chapter 2): bytes -> subwords.

A minimal byte-level BPE, built up to match the chapter. Stubs for now.
"""

from __future__ import annotations


class BPETokenizer:
    """Byte-pair-encoding tokenizer over raw UTF-8 bytes."""

    def train(self, text: str, vocab_size: int) -> None:
        """Learn merges from `text` up to `vocab_size` tokens."""
        raise NotImplementedError

    def encode(self, text: str) -> list[int]:
        raise NotImplementedError

    def decode(self, ids: list[int]) -> str:
        raise NotImplementedError
