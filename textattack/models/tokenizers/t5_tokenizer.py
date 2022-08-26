"""
T5 Tokenizer
---------------------------------------------------------------------

"""

import transformers


class T5Tokenizer:
    """Uses the T5 tokenizer to convert an input for processing.

    For more information, please see the T5 paper, "Exploring the Limits of
    Transfer Learning with a Unified Text-to-Text Transformer".
    Appendix D contains information about the various tasks supported
    by T5.

    Supports the following modes:

    * summarization: summarize English text
    * english_to_german: translate English to German
    * english_to_french: translate English to French
    * english_to_romanian: translate English to Romanian
    """

    def __init__(self, mode="english_to_german", max_length=64):
        if mode == "english_to_german":
            self.tokenization_prefix = "translate English to German: "
        elif mode == "english_to_french":
            self.tokenization_prefix = "translate English to French: "
        elif mode == "english_to_romanian":
            self.tokenization_prefix = "translate English to Romanian: "
        elif mode == "summarization":
            self.tokenization_prefix = "summarize: "
        else:
            raise ValueError(f"Invalid t5 tokenizer mode {mode}.")

        self.tokenizer = transformers.AutoTokenizer.from_pretrained(
            "t5-base", use_fast=True
        )
        self.max_length = max_length

    def __call__(self, text, *args, **kwargs):
        """
        Args:
            text (:obj:`str`, :obj:`List[str]`):
                    The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings.
        """
        assert isinstance(text, str) or (
                isinstance(text, (list, tuple))
                and (len(text) == 0 or isinstance(text[0], str))
        ), "`text` must be a string or a list of strings."
        if isinstance(text, str):
            text = self.tokenization_prefix + text
        else:
            for i in range(len(text)):
                text[i] = self.tokenization_prefix + text[i]
        return self.tokenizer(text, *args, max_length=self.max_length, **kwargs)

    def decode(self, ids):
        """Converts IDs (typically generated by the model) back to a string."""
        return self.tokenizer.decode(ids)
