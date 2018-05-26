from sys import implementation
if(implementation.name == 'micropython'):
	import urequests
else:
	import requests as urequests
import cmd
	
update_server = "http://localhost:8000/"

def remote_exec(url):
	response = urequests.get(url)
	try:
		exec(response.content)
	except Exception as e:
		print("Remote exec error" + repr(e))
	finally:
		response.close()


def check_update(ver):
	if(not ver in ["stable", "previous"]):
		raise TypeError("ver should be one of stable&previous")
	response = urequests.get(update_server+'api.php?q=check_update&a={"version":"%s"}'%(ver))
	r = response.json()
	response.close()
	return r


def rm_all():
	cmd.rm("./core")