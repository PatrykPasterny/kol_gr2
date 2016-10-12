class Matrix:
	def __init__(self, a11,a12,a21,a22):
		self.a11=a11
		self.a12=a12
		self.a21=a21
		self.a22=a22
		
	def add(self, second):
		self.a11+=second.a11
		self.a12+=second.a12
		self.a21+=second.a21
		self.a22+=second.a22
		return self
	
		
	def printf(self):
		print "Element a11 wybranej macierzy 2x2 jest rowny: %s" %self.a11
		print "Element a11 wybranej macierzy 2x2 jest rowny: %s" %self.a12
		print "Element a11 wybranej macierzy 2x2 jest rowny: %s" %self.a21
		print "Element a11 wybranej macierzy 2x2 jest rowny: %s" %self.a22
	
a=Matrix(1,2,3,4)
a.printf()
b=Matrix(2,3,4,5)
c=a.add(b)

print "\n"
c.printf()
