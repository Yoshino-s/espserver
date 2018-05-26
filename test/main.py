import urequests
import update_manager as um

cmds=[
	{
		"option": "create_folder",
		"path": "/sdcard/test/"
	}, {
		"option": "create_file",
		"path": "/sdcard/test/t.py",
		"src": "http://localhost:8000/t.py"
	}, {
		"option": "delete_file",
		"path": "/sdcard/test/t.py"
	}, {
		"option": "delete_folder",
		"path": "/sdcard/test/"
	}
]

for cmd in cmds:
	um.load_update_command(cmd)