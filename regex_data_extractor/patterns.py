"""Regular expressions for extracting common data types from text.
From the text provided the logic will find the correct match.This is where the whole work of extraction takes place
so re.findall returns all correct matches
"""
from __future__ import annotations
import re 

PATTERNS = {
    # local part, mandatory @, domain labels, TLD of 2+ letters
    "email": r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)*\.[A-Za-z]{2,}\b",

    # http/https, domain, optional path; the path must end on a word
    # character or "/" so trailing punctuation ("see https://x.com.") is excluded
    "url": r"https?://[\w-]+(?:\.[\w-]+)+(?:/\S*[\w/#?=&%-])?",

    # (123) 456-7890, 123-456-7890, 123.456.7890; not part of a longer digit run
    "phone": r"(?<!\d)(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}(?!\d)",

    # four groups of four digits separated by a space or dash
    "card": r"(?<!\d)\d{4}[ -]\d{4}[ -]\d{4}[ -]\d{4}(?!\d)",

    # 12-hour (1-12, AM/PM) tried first, then 24-hour (00-23)
    "time": r"\b(?:(?:1[0-2]|0?[1-9]):[0-5]\d\s?[AaPp][Mm]|(?:[01]?\d|2[0-3]):[0-5]\d)\b",

    # opening, closing or self-attributed tags; must start with a letter,
    # so "a < b > c" and "<3" are not tags
    "html": r"</?[A-Za-z][^<>]*>",

    # # followed by a letter, not preceded by a word character (lookbehind feature)
    "hashtag": r"(?<!\w)#[A-Za-z]\w*",

    # $19.99, $1,234.56, $5; comma groups need exactly 3 digits
    "currency": r"\$(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d{2})?",
}

COMPILED = {name: re.compile(p) for name, p in PATTERNS.items()}


def extract(kind: str, text: str) -> list[str]:
    """Return every match of the given data type found in text."""
    return COMPILED[kind].findall(text)
