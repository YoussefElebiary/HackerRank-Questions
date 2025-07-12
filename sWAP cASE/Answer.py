def swap_case(s: str):
    ans = ""
    for c in s:
        if c.islower():
            ans += c.upper()
        else:
            ans += c.lower()
    return ans