def check_palindrome(text):
  if(len(text) <= 1): 
    return False
  val = text.strip().lower().replace(' ', '')
  reverse = val[::-1]
  return val == reverse


if __name__ == "__main__":
    print(check_palindrome('Noon'))