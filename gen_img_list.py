#!python3
import os
from xml.dom.minidom import parse,getDOMImplementation

WORK_DIR="."+os.sep+"img"
XML_FILE="."+os.sep+"img_list.xml"




class HandleXml:

	img_character=["category","description"]
	
	def __init__(self, work_dir, xml_file):
		self.work_dir=work_dir
		self.xml_file=xml_file
		self.xml = parse(XML_FILE)
		self.top_el = self.xml.documentElement
		self.file_list=[]
		self._trvaversal()
		self.add_el()
		print(self.toprettyxml())
		
	def _trvaversal(self,):
		filelist=os.listdir(self.work_dir)
		for fname in filelist:
			url=os.path.join(self.work_dir,fname)
			#print(url)
			if os.path.isfile(url):
				self.file_list.append([url, ])
			elif os.path.isdir(url):
				l=os.listdir(url)
				for f in l:
					u=os.path.join(url,f)
					#print(u)
					if os.path.isfile(u):
						self.file_list.append([u, fname])
				

	def add_el(self):
		child=self.top_el.getElementsByTagName("url")
		self.urls={}
		for i in child:
			#delete repeate
			self.urls[i]=1
		for i in self.file_list:
			url=i[0]
			try:
				self.urls[url]
			except:
				#print(url)
				m=self.xml.createElement("img")
				u=self.xml.createElement("url")
				t=self.xml.createTextNode(url)
				
				u.appendChild(t)
				m.appendChild(u)
				self.top_el.appendChild(m)

	def toprettyxml(self):
		return self.xml.toprettyxml()

	def write_xml(self):
		try:
				with open(self.xml_file,'w',encoding='UTF-8') as f:
					self.xml.writexml(f,indent='',addindent='\t',newl='\n',encoding='UTF-8')
					print('OK')
		except Exception as err:
			print(err)
		
handle_xml=HandleXml(WORK_DIR,XML_FILE)
handle_xml.write_xml()
			
def to_xml(base_dir,fname):
	pass


