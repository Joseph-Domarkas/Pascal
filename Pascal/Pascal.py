
from beaker.middleware import SessionMiddleware
import re


class Pascal___class___ ( ):
	
	class wsgi___class___ ( ):
		
		session_option = {
			'session.cookie_expires': True
		}
		
		def index (self, tensor, flow):
			flow ('200 OK', [('Content-Type','text/html')])
			return [b"Index"]
			
		def hello (self, tensor, flow):
			flow ('200 OK', [('Content-Type','text/html')])
			h = tensor ['Dangardas.url_argument']
			r = "Hello/".encode ("utf-8")
			for i in h:
				i = i. encode("utf-8")
				r = r + i
			return [bytes(r)]
		
		urls = [
			(r'/^$', index),
			(r'/hello/?$', hello),
			(r'/hello/(.+)$', hello),
		]
		
		
		def application_mark (self, tensor, flow):
			
			flow ('200 OK', [('Content-Type','text/html')])
			if tensor ['REQUEST_METHOD'] == 'GET' and tensor ['PATH_INFO'] == '/ab':
				return [b"Hello World!!!@ab"]
			elif tensor ['REQUEST_METHOD'] == 'GET' and tensor ['PATH_INFO'] == '/orion':
				return [b"ORION!"]
			else:
				print (tensor)
				session = tensor ['beaker.session']
				path = tensor ['PATH_INFO']
				for regex, callback in self. urls:
					match = re.search(regex, path)
					if match is not None:
						tensor ['Dangardas.url_argument'] = match.groups()
						return callback (self, tensor, flow)
				return [b"Not found."]

		def route_mark (self, path):
			pass
		
		def __init__ (self):
			self. application = SessionMiddleware (self. application_mark, self. session_option)
			self. urls = self. urls
		
	
	def __init__ (self):
		
		self. x = True
		self. y = 1000
		self. wsgi = self. wsgi___class___ ( )
		
	
