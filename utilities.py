jummal_values = [
    ("أ", 1),
    ("ب", 2),
    ("ج", 3),
    ("د", 4),
    ("هـ", 5),
    ("و", 6),
    ("ز", 7),
    ("ح", 8),
    ("ط", 9),
    ("ي", 10),
    ("ك", 20),
    ("ل", 30),
    ("م", 40),
    ("ن", 50),
    ("س", 60),
    ("ع", 70),
    ("ف", 80),
    ("ص", 90),
    ("ق", 100),
    ("ر", 200),
    ("ش", 300),
    ("ت", 400),
    ("ث", 500),
    ("خ", 600),
    ("ذ", 700),
    ("ض", 800),
    ("ظ", 900),
    ("غ", 1000)
]

def get_jummal_value(letter):
    """
    Returns the jummal value for a given Arabic letter.
    If the letter is not found, returns None.
    """
    for char, value in jummal_values:
        if char == letter:
            return value
    return None 

def get_jummal_sum(text):
    """
    Calculates the jummal sum of a given Arabic text.
    Only considers letters that have jummal values.
    """
    total = 0
    for char in text:
        value = get_jummal_value(char)
        if value is not None:
            total += value
    return total    

def get_ayat_from_to(start_aya, end_aya):
    """
    Retrieves Ayat objects from the database for a given sura and range of ayas.
    """
    from models import Ayat

    if start_aya > end_aya:
        raise ValueError("start_aya must be less than or equal to end_aya")
    if start_aya < 1 or end_aya < 1:
        raise ValueError("start_aya and end_aya must be positive integers")
    if start_aya == end_aya:
        selected_ayats = Ayat.query.filter(Ayat.num_aya == start_aya).order_by(Ayat.num_aya).all()
    else:
        selected_ayats = Ayat.query.filter(Ayat.num_aya >= start_aya, 
                                            Ayat.num_aya <= end_aya).order_by(Ayat.num_aya).all()
    return " ".join(selected_ayats)