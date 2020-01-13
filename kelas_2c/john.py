import csv
import matplotlib
from matplotlib import pyplot as plt
import request
import sqlite3
from matplotlib import style

class Doyok(self):
	"""docstring for ClassName"""
	def __init__(self, kode):
		self.kode = kode

	def function(self):
		with open('kelas_2c/Kevin.csv','r') as harga:
			reader = csv.reader(harga)
			for row in reader:
				if str(row[0]) == self.kode:
					print("Kode barang",row[0],"nama barang",row[1],"jumlah",row[2],"harga",row[3])
    def paijo():
days = [1,2,3,4,5]
running =[7,8,6,11,7]
reading = [2,3,4,3,2]
swimming =[7,8,7,2,2]
dancing = [8,5,7,8,13]
slices = [7,2,8,8]
activities = ['running','reading','swimming','dancing']
cols = ['c','m','r','b']
plt.pie(slices,
 labels=activities,
 colors=cols,
 startangle=90,
 shadow= True,
 explode=(0,0.1,0,0),
 autopct='%1.1f%%')
plt.title('Activities')
plt.show()
	def tono():
x = [5,2,7]
y = [2,16,4]
plt.plot(x,y)
plt.title('Info')
plt.ylabel('Sumbu Y')
plt.xlabel('Sumbu X')
plt.show()
	def dodo(): 
style.use('ggplot')
x = [5,8,10]
y = [12,16,6]
x2 = [5,9,11]
y2 = [8,8,6]
plt.plot(x,y,'g',label='Macet', linewidth=1)
plt.plot(x2,y2,'c',label='Lancar',linewidth=1)
plt.title('Info Lalu lintas')
plt.ylabel('X')
plt.xlabel('Y')
plt.legend()
plt.show()
	def lakso():
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="Nike",color='m',width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Adidas", color='r',width=.5)
plt.legend()
plt.xlabel('Bulan')
plt.ylabel('Pasang')
plt.title('Info Penjualan Sepatu')
plt.show()
	def Create():
        try:
            self.connection = sqlite3.connect('./kelas_2c/tukiem.db')
            self.cursor = self.connection.cursor()

            self.cursor.execute('CREATE TABLE Tukiem (id INTEGER PRIMARY KEY, nama VARCHAR(50), jumlah VARCHAR(50))')
        except:
            print("Tabel Gagal Cok!")

    def InputData():
        try:
            self.cursor.execute('INSERT INTO tukiem VALUES(?, ?, ?)', (1, "Tukiem", "2"))
            self.cursor.execute('INSERT INTO tukiem VALUES(?, ?, ?)', (2, "Bin", "4"))
            self.cursor.execute('INSERT INTO tukiem VALUES(?, ?, ?)', (3, "Titan", "3"))
            self.connection.commit()
        except:
            print("Tabel Gagal Cok!")

    def ViewData():
        self.cursor.execute('SELECT * FROM Tukiem')
        row = self.cursor.fetchone()

        nama = row[1]
        rupiah = row[2]

        print("nama : " + str(nama))
        print("jumlah : " + str(jumlah))
        self.connection.commit()
    def asep():
r = requests.get('https://www.wikipedia.org/')
print(r.text)