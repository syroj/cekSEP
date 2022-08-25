import glob
import pdfplumber
import numpy
import pandas as pd

tanggal =input("Tanggal: ") # input tanggal
key = tanggal+'//*.pdf' # membuat keyword
file = glob.glob(key) # buat list file
files = pd.DataFrame(file) # buat dataframe File
sep =[] #buat list SEP kosong
print("Loading...") # loading
# proses extraksi nomor SEP
for fi in file:
	klaim = pdfplumber.open(fi)
	for page in klaim.pages:
		for line in page.extract_text().splitlines():
			if "nomor sep :" in line.lower():
				sep.append(line.split()[-1])
#Ekstraksi selesai

no_sep=pd.DataFrame(sep)
result=pd.concat([files,no_sep],axis=1)
# print(result)
result.to_csv(tanggal+'.csv', index=False)
print("Selesai") #informasi proses selesai