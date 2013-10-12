#!/usr/bin/python3

import random
import string
from subprocess import call

gpid = 0

class License:
	def __init__(self, fun, lid, kpass):
		self.fun = fun
		self.lid = lid
		self.kpass = kpass

class Developer:
	def __init__(self, name):
		global gpid
		self.licenses = {}
		self.dependency = []
		self.name = name
		gpid = gpid + 1
		self.pid = gpid
	
	def buy(self, swh):
		if swh not in self.licenses:
			self.licenses[swh] = []
		self.licenses[swh].append(swh.license(self.name, self.pid))
	
	def link(self, lb):
		request = {}
		f = open('developer/keys.h', 'w')
		for d in self.dependency:
			license = self.licenses[d].pop()
			f.write('#define SWH_{}_KEY "{}"\n'.format(license.fun, license.kpass))
			request[d] = {'name': self.name, 'pid': self.pid, 'license': license.lid}
		f.close()
		lb.link(request)

class LinkBroker:
	def link(self, request):
		for (d, i) in request.items():
			d.request(i['name'], i['pid'], i['license'])
		if call(['make']) != 0:
			print("Linking failed.")

class SoftWareHouse:
	def __init__(self, fun):
		self.fun = fun
		self.db = {}
	
	def license(self, name, pid):
		kpass = ''.join([random.choice(string.digits+string.ascii_letters) for i in range(8)])
		lid = ''.join([random.choice(string.digits) for i in range(8)])
		self.db[(name, pid, lid)] = kpass
		return License(self.fun, lid, kpass)
	
	def request(self, name, pid, license):
		f = open('{}/key.h'.format(self.fun), 'w')
		if (name, pid, license) in self.db:
			f.write('#define KEY "{}"\n'.format(self.db[(name, pid, license)]))
			del self.db[(name, pid, license)]
		f.close()

#print("Developer requests license...")
dev = Developer('Bob')
swh1 = SoftWareHouse('swh1')
swh2 = SoftWareHouse('swh2')
dev.dependency.append(swh1)
dev.dependency.append(swh2)
dev.buy(swh1)
dev.buy(swh2)

lb = LinkBroker()
dev.link(lb)
