"""Compare document revisions and surface changed numbers for review."""
from runtime import *

import difflib
import hashlib
import re
from collections import Counter
def process(data):
    before,after=data["before"],data["after"]
    if not isinstance(before,str) or not isinstance(after,str): raise ValueError("before and after must be strings")
    if any(len(s)>200000 or len(s.splitlines())>5000 for s in (before,after)):
        raise ValueError("each document is limited to 200000 characters and 5000 lines")
    cap=integer(data.get("max_diff_lines",1000),"max_diff_lines",1)
    if cap>10000: raise ValueError("max_diff_lines exceeds 10000")
    a,b=before.splitlines(),after.splitlines()
    removed=added=0
    for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
        if tag in ("delete","replace"): removed+=j-i
        if tag in ("insert","replace"): added+=l-k
    diff=list(difflib.unified_diff(a,b,fromfile=str(data.get("before_label","before")),tofile=str(data.get("after_label","after")),lineterm=""))
    pattern=r"(?<!\w)[+-]?\d+(?:[.,]\d+)*(?:%)?"
    left,right=Counter(re.findall(pattern,before)),Counter(re.findall(pattern,after))
    return {"added_lines":added,"removed_lines":removed,"numbers_removed":list((left-right).elements()),"numbers_added":list((right-left).elements()),"unified_diff":"\n".join(diff[:cap]),"truncated":len(diff)>cap,"before_sha256":hashlib.sha256(before.encode()).hexdigest(),"after_sha256":hashlib.sha256(after.encode()).hexdigest()}

if __name__ == "__main__":
    sys.exit(main(process, "Compare document revisions and surface changed numbers for review."))
