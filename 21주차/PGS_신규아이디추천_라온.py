# regex, lower() !!! 

import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('[.]{2,}', '.', new_id)
    new_id = new_id.lstrip('.').rstrip('.')
    if not new_id:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    new_id = new_id.rstrip('.')
    while len(new_id) <= 2:
        new_id += new_id[len(new_id)-1]
    return new_id

### 이전 풀이
import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^a-z0-9-_.]", "", new_id)
    new_id = re.sub("[.]{2,}", ".", new_id)
    new_id = re.sub("^[.]|[.]$", "", new_id)
    new_id = "a" if not new_id else new_id 
    new_id = new_id[:15] if len(new_id) > 15 else new_id
    new_id = re.sub("[.]$", "", new_id)
    while len(new_id) < 3:
        new_id = new_id + new_id[len(new_id)-1]*1
    return new_id