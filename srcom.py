import serial, glob, sys
import tkinter as tk
from tkinter.colorchooser import askcolor



###################################################################################################################################


comm_ports = []
check = False
data = [ "\xFF\xFF\xFF", "\xFF\xFF\x00", "\x00\xFF\x00", "\x00\x00\xFF", "\xFF\x00\x00", "\xFF\x00\xFF", "\x00\xFF\xFF", "\x00\x00\x00" ]


###################################################################################################################################


class SerialWrapper:

	def __init__(self, device):
		self.ser = serial.Serial(port= device,
			  baudrate= 115200,
			  parity= serial.PARITY_NONE,
			  stopbits= serial.STOPBITS_ONE,
			  bytesize= serial.EIGHTBITS,
			  timeout= 1)

	def sendData(self, data):
		data += "\r\n"
		self.ser.write(data.encode())

def send_packet(i):
	if check:
		ser = SerialWrapper(comm_ports[0])
		while 1:
			if ser.isOpen():
				try:
					ser.flushInput()
					ser.flushOutput()
					ser.write(bytes(data[i],'iso-8859-1'))
				except:
					pass

def connect_to_serial_port():
	global comm_ports, check
	if sys.platform.startswith('win'):
		ports = ['COM%s' % (i + 1) for i in range(256)]
	elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
		ports = glob.glob('/dev/tty[A-Za-z]*')
	for p in ports:
		try:
			s = serial.Serial(p)
			s.close()
			comm_ports.append(p)
			check = True
		except (OSError, serial.SerialException):
			pass

def get_color():
	  color = askcolor()


###################################################################################################################################


def main():
	mw = tk.Tk()
	mw.title("Serial Color Picker")
	mw.geometry("435x195")
	back = tk.Frame(master=mw,bg= "grey")
	back.pack_propagate(0)
	back.pack(fill=tk.BOTH, expand=1)

	tk.Button(master= back, width= 10, height= 4, command= lambda: send_packet(0), bg= "white").grid(row=0, column=0)
	tk.Button(master= back, width= 10, height= 4, command= lambda: send_packet(1), bg= "yellow").grid(row=0, column=1)
	tk.Button(master= back, width= 10, height= 4, command= lambda: send_packet(2), bg= "green").grid(row=0, column=2)
	tk.Button(master= back, width= 10, height= 4, command= lambda: send_packet(3), bg= "blue").grid(row=0, column=3)

	tk.Button(master= back, width= 10, height= 4, command= lambda: send_packet(4), bg= "red").grid(row=1, column=0)
	tk.Button(master= back, width= 10, height= 4, command= lambda: send_packet(5), bg= "pink").grid(row=1, column=1)
	tk.Button(master= back, width= 10, height= 4, command= lambda: send_packet(6), bg= "cyan").grid(row=1, column=2)
	tk.Button(master= back, width= 10, height= 4, command= lambda: send_packet(7), bg= "black").grid(row=1, column=3)

	tk.Button(master = back, text= "Connect", width= 10, height= 2, command= connect_to_serial_port).grid(row=4, column=0)
	tk.Button(master = back, text= "Exit", width= 10, height= 2, command= mw.destroy).grid(row=4, column=3)

	mw.mainloop()


###################################################################################################################################


if __name__ == '__main__':
	main()


####################################################################################################################################
