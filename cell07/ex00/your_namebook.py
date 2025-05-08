#!/usr/bin/env python3

import re

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
cleaned_list = []
for text in persons:
    clean = re.sub(r'[^a-zA-Z0-9\s]', '',text)
    cleaned_list.append(clean)
print(cleaned_list)