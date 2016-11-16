class Tensor(object):
	
	def __init__(self, elements):
		self.elements=elements
		
	def __repr__(self):
		end_message=""
		for w in self.elements:
			end_message+="("
			for k in w:
				if k>=0:
					if k<10:
						end_message+=" %.2f " %k
					else:
						end_message+=" %.1f " %k
				else:
					if k>-10:
						end_message+="%.2f " %k
					else:
						end_message+="%.1f " %k
 			end_message+=")\n"
		return end_message
		
	def trans(self):
		for w in range(len(self.elements)):
			for k in range(w,len(self.elements[w])):
				temporary_variable=self.elements[w][k]
				self.elements[w][k]=self.elements[k][w]
				self.elements[k][w]=temporary_variable	
	
	def track(self):
		count=0
		for w in range(len(self.elements)):
			for k in range(len(self.elements[w])):
				if k==w:
					count+=self.elements[w][k]
		return count
		
	def __add__(self,other):
		new_elements=[]
		lines=[]
		N=len(self.elements)
		if N==len(other.elements):
			for w in range(N):
				for k in range(N):
					new_element=self.elements[w][k]+other.elements[w][k]
					lines.append(new_element)
				new_elements.append(lines)
				lines=[]
			return Tensor(new_elements)
		else:
			print "Nie da sie dodac tych macierzy."
	
	def __radd__(self,x):
		for w in range(len(self.elements)):
			for k in range(len(self.elements[w])):
				self.elements[w][k]+=x
		return self
			
	def __sub__(self,other):
		new_elements=[]
		lines=[]
		N=len(self.elements)
		if N==len(other.elements):
			for w in range(N):
				for k in range(N):
					new_element=self.elements[w][k]+other.elements[w][k]
					lines.append(new_element)
				new_elements.append(lines)
				lines=[]
			return Tensor(new_elements)
		else:
			print "Nie da sie odjac tych macierzy."
		
	def __mul__(self,other):
		if len(self.elements[0])==len(other.elements):
			new_elements=[]
			lines=[]
			index=0
			
			for w in range(len(self.elements)):
				while len(lines)<len(self.elements):
					for k in range(len(other.elements)):
						index+=self.elements[w][k]*other.elements[k][len(lines)]
					lines.append(index)
					index=0
				new_elements.append(lines)
				lines=[]
			return Tensor(new_elements)
		else:
			print "Nie da sie pomnozyc tych macierzy."
		
	def __pow__(self, x):
		if x>1:
			new_tensor=self
			for n in range(x-1):
				new_tensor = self*new_tensor
			return new_tensor
		elif x==1:
			return self
		else: 
			print "Prosze podac macierz odwrotna do podanej."


def make_tensor(N):
	line=[]
	for w in range(N):
		for k in range(N):
			line.append(float(raw_input("Podaj element wiersza macierzy: ")))
		yield line
		line=[]
		
	
		
