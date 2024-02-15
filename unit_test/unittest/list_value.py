data = "Python is a best language"

def create_value(data_str):
  input_data = data_str.split()
  result = []
  for index in range(len(input_data)):
    result.append((index, input_data[index]))
  print(result)
  return result

if __name__ == "__main__":
    print(create_value(data))