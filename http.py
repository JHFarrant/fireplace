import json
import subprocess
from nameko.web.handlers import http

FIREPLACE_VIDEO_FILE_PATH = "/home/pi/fireplace.webm"

class HttpService:
	name = "http_service"

	@http("POST", "/light_fireplace")
	def light_fireplace(self, request):
		#
		subprocess.call(["omxplayer", FIREPLACE_VIDEO_FILE_PATH])
		subprocess.call(["echo 'as' | cec-client RPI -s -d 1"])

		return json.dumps({"message":"Fireplace lit successfully"})