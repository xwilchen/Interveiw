"""
Please use Python 3 to answer question
Welcome to answer with unit testing code if you can
 
After you finish coding, please push to your GitHub account and share the link with us.
"""
 
# Please write a function to reverse the following nested input value into output value
 
# Input:
input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}
 
# Output:
output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}

# Answer:
def invert_dict(dic, previous=None):
  if isinstance(dic, str):
    return {dic: previous}
  else:
    key = list(dic.keys())[0]
    if previous:
      return invert_dict(dic.get(key), previous={key: previous})
    else:
      return invert_dict(dic.get(key), previous=key)