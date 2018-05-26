import sys
workspace_path = "/sdcard/workspace/espserver/"
sys.path.append(workspace_path + "./lib/")

import cmd, update_manager
import urequests as requests

update_manager.remote_exec("http://localhost:8000/t.py")