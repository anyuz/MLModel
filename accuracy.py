import pandas as pd
with open("results.txt”) as file:  
  data = file.read() 
data = data.split()
def test_answer():
    assert int(data[0]) > int(data[1])
