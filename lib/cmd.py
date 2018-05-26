from sys import implementation
if(implementation.name == 'micropython'):
	import uos
	import urequests
	from uhashlib import sha1
	from ubinascii import hexlify
else:
	import os as uos
	import requests as urequests
	from hashlib import sha1
	from binascii import hexlify
import stat


try:
	uos.listdir()
	listdir = uos.listdir
except AttributeError:
	listdir = lambda p : [x[0] for x in uos.ilistdir(p) if not x[0] in ['.', '..']]
__all__ = ["exists", "ls", "rm", "pwd", "mkdir", "cd", "mv", "saveas"]

def exists(path):
	try:
		uos.stat(path)
		return True
	except OSError:
		return False


def ls(path="./"):
	return listdir(path)


def mkdir(path):
	uos.mkdir(path)


def cd(path="/"):
	uos.chdir(path)
	

def pwd():
	return uos.getcwd()


def rm(path):
	if(not exists(path)):
		raise OSError(2,)
	if(stat.S_ISDIR(uos.stat(path)[stat.ST_MODE])):
		li = listdir(path)
		for i in li:
			rm(path+'/'+i,forced)
		uos.rmdir(path)
	else:
		uos.remove(path)


def mv(fpath, tpath):
	uos.rename(fpath, tpath)


def saveas(url, path):
	a = urequests.get(url)
	with open(path, 'wb') as file:
		file.write(a.content)
	a.close()


def tree(path):
	if(not exists(path)):
		raise OSError(2,)
	if(stat.S_ISDIR(uos.stat(path)[stat.ST_MODE])):
		l = {}
		li = listdir(path)
		for i in li:
			l[i] = tree(path+'/'+i)
		return l
	else:
		with open(path, "rb") as file:
			sha1v = sha1()
			sha1v.update(file.read())
			return hexlify(sha1v.digest())
