import pandas as pd
import subprocess

# Take in user input i.e. how large they would like the dataset to be
sizeofdataset = input("large would you like the dataset? (1 to 36400)")
sizeofdataset = int(sizeofdataset) + 2 # Size has to be size + 2 as the json file has 2 extra lines before the urls begin

# Use the Panda package to read the json file and convert to a CSV
df = pd.read_json('data_legitimate_36400.json')
df.to_csv('data.csv')

filename = str(sizeofdataset -2)  # Set filename 


# Use Linux terminal commands to parse the output nicely and save to a final file titled 'numberofurls'.csv
subprocess.run("head -" + str(sizeofdataset -1) + " data.csv > " + "temp1.csv", shell = True)
subprocess.run("sed '1d' temp1.csv > temp2.csv", shell = True)
subprocess.run("sed 's/^.*,//' temp2.csv > " + filename+"urls.csv", shell = True)
subprocess.run("rm -f data.csv temp1.csv temp2.csv", shell = True)
