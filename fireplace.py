import json
import subprocess
from nameko.web.handlers import http
from time import sleep

FIREPLACE_VIDEO_FILE_PATH = "/home/pi/fireplace2.mp4"

class FireplaceHttpService:
	name = "fireplace_http_service"

	@http("POST", "/light_fireplace")
	def light_fireplace(self, request):
		#
		subprocess.Popen(["omxplayer", "--pos","00:00:25", FIREPLACE_VIDEO_FILE_PATH, "&"], close_fds=True)
		sleep(1)
		subprocess.Popen(["echo", "'as'", "|", "cec-client", "RPI", "-s", "-d", "1"], close_fds=True)

		return json.dumps({"message":"Fireplace lit successfully"})