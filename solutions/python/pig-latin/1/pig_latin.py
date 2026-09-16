def begins_w_vowel(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return text.lower().startswith(tuple(vowels))
        
def has_vowel(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return any(char in vowels for char in text)

def get_vowels(text):
    # This filters the string and joins the vowels back into a new string
    return "".join([char for char in text if char in "aeiouAEIOU"])

def starts_w_xr_or_yt(text): 
    str = ['xr', 'yt']
    return text.lower().startswith(tuple(str))




def has_qu(text): 
    first_vowel = None 
    for i, char in enumerate(text.lower()): 
        if char in 'aeiou': 
            first_vowel = i 
            break 
    
    qu_position = text.lower().find('qu') 
    return qu_position != -1 and qu_position < first_vowel

def con_followed_by_y(text):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if text.lower().startswith(tuple(vowels)):
        return False

    for i, char in enumerate(text.lower()):
        if char == 'y':
            return i > 0

        if char in vowels:
            return False

    return False
 
    
    


def translate(text):

    if ' ' in text:
        return ' '.join(translate(word) for word in text.split())
    
    if begins_w_vowel(text) or starts_w_xr_or_yt(text):
        return text + 'ay'
    elif has_qu(text):
        if text.lower().startswith('qu'):
            qu = text[:2]
            rest = text[2:]
            return rest + qu + 'ay'
        else:
            position = text.lower().find('qu') 
            before = text[:position] 
            match = text[position:position + 2] 
            after = text[position + 2:] 
            return after + before + match + 'ay'
    elif con_followed_by_y(text):
        position = text.lower().find('y') 
        before = text[:position] 
        after = text[position:] 
        return after + before + 'ay'
    else:
        for i, char in enumerate(text.lower()): 
            if char in 'aeiou': 
                return text[i:] + text[:i] + 'ay' 
        return text + 'ay'
            
        
    pass
