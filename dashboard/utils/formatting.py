def abbreviate_number(n):
    """
    Abrevia números grandes:
    1.000 → 1K
    1.500.000 → 1.5M
    2.000.000.000 → 2B
    """
    if n >= 1_000_000_000:
        return f"{n/1_000_000_000:.1f}B"
    elif n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n/1_000:.1f}K"
    else:
        return str(n)