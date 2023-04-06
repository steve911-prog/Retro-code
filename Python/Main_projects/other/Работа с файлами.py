вмаавм ш9Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f = open("NEW.txt", "r")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    f = open("NEW.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'NEW.txt'
>>> f = open("C:/Users/hryts/Desktop/NEW.txt", "r")
>>> f.read()
'РЎРµРіРѕРґРЅСЏ РІРѕСЃРєСЂРµСЃРµРЅСЊРµ\n27.09.2020'
>>> f.close()
>>> f = open("C:/Users/hryts/Desktop/NEW.txt", "r")
>>> f.read()
'Hello, world!\n27.09.2020'
>>> f.read(4)
''
>>> f.read(5)
''
>>> f.close()
>>> f = open("C:/Users/hryts/Desktop/NEW.txt", "r")
>>> f.read(5)
'Hello'
>>> f.readline()
', world!\n'
>>> f.close()
>>> f = open("C:/Users/hryts/Desktop/NEW.txt", "r")
>>> for line in f:
	print(line)

	
Hello, world!

27.09.2020
>>> f.closed()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    f.closed()
TypeError: 'bool' object is not callable
>>> f.closed
False
>>> f.mode
'r'
>>> f.name
'C:/Users/hryts/Desktop/NEW.txt'
>>> f.close()
>>> f.closed
True
>>> f = open("C:/Users/hryts/Desktop/NEW.txt", "a")
>>> f.write(" Test")
5
>>> f.read()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    f.read()
io.UnsupportedOperation: not readable
>>> f.write('\n Hello!')
8
>>> f.close()
>>> f = open("C:/Users/hryts/Desktop/NEW.txt", "r")
>>> f.tell()
0
>>> f.read(7)
'Hello, '
>>> f.tell()
7
>>> f.seek(9)
9
>>> f.read(3)
'rld'
>>> f.seek(0)
0
>>> f.read()
'Hello, world!\n27.09.2020 Test\n Hello!'
>>> f.close()
>>> with open("C:/Users/hryts/Desktop/NEW.txt", "r") as f:
	for list in f:
		print(list)

		
Hello, world!

27.09.2020 Test

 Hello!
>>> f.closed
True
>>> f = open("C:/Users/hryts/Desktop/NEW2.txt", "x")
>>> f.close()
>>> 
