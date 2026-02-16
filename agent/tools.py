def analyze_error(error: str):
    if "IndexError" in error:
        return "List index out of range. Check loop bounds."
    if "KeyError" in error:
        return "Dictionary key missing."
    return "Unknown error."


def review_code(code: str):
    issues = []

    if "print(" in code:
        issues.append("Use logging instead of print.")

    if "== None" in code:
        issues.append("Use 'is None'.")

    if not issues:
        return "No issues found."

    return "\n".join(issues)
