from invert_dict import invert_dict

def test_default():
    assert(invert_dict({'hired': {'be': {'to': {'deserve': 'I'}}}}) == {'I': {'deserve': {'to': {'be': 'hired'}}}})