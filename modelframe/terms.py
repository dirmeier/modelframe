import re


def get_random_effects_terms(rhs):
    ext = _find_within(rhs, r"\(.*?\)")
    terms = []

    for ex in ext:
        terms.append(_ranef_strip(ex.group(0)))

    if not re.match(r".*\(.*\).*", rhs) and "|" in rhs:
        if all(x in rhs for x in ["|", "+"]):
            raise ValueError("your formula isn't built correctly")
        terms.append(_ranef_strip(rhs))

    return terms


def get_fixed_effects_terms(rhs):
    ext = _find_within(rhs, r"\(.*?\)")

    for ex in ext:
        rhs = _coef_strip(rhs, ex)

    terms = []
    els = rhs.split("+")
    for el in els:
        el = el.strip()
        if el != "" and "|" not in el:
            terms.append(el)
        elif el == "":
            raise ValueError("your formula isn't built correctly")
    return terms


def _find_within(text, pattern):
    return re.finditer(pattern, text)


def _search(text, pattern):
    return re.search(pattern, text)


def _coef_strip(coef, ex):
    return coef.replace(ex.group(0), "").rstrip(r" |+").lstrip(" |+")


def _ranef_strip(ranef):
    return ranef.strip().rstrip(")").lstrip("(").replace(" ", "")
