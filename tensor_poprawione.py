from test_poprawione import Tensor,make_tensor

def main():
	N=3
	init_tensor=[]
	for w in make_tensor(N):
		init_tensor.append(w)
	my_tensor=Tensor(init_tensor)
	print "TENSOR STARTOWY"
	print my_tensor
	my_tensor.trans()
	print "SLAD TENSORA STARTOWEGO"
	print my_tensor.track()
	print "TENSOR TRANSPONOWANY"
	print my_tensor
	my_tensor.trans()
	my_tensor=Tensor([[1,2,3],[-1,-2,-3],[4,-5,6]])
	print "SUMA MACIERZY:\n ( 1 , 2 , 3 )   ( 1 , 2 , 3 ) \n ( 3 , 4 , 5 ) + (-1 ,-2 ,-3 ) \n ( 6 , 7 , 8 )   ( 4 ,-5 , 6 )\n"
	other_tensor=Tensor([[1,2,3],[3,4,5],[6,7,8]])
	print my_tensor+other_tensor
	other_tensor=Tensor([[1,2,3],[-1,-2,-3],[4,-5,6]])
	print "ROZNICA MACIERZY:\n ( 1 , 2 , 3 )   ( 0 , 1 , 2 ) \n (-1 ,-2 ,-3 ) - ( 1 , 2 , 3 ) \n ( 4 ,-5 , 6 )   ( 5 , 3 , 1 ) \n"
	print my_tensor-other_tensor
	print "MNOZENIE MACIERZY:\n ( 1 , 2 , 3 )   ( 0 , 1 , 2 ) \n (-1 ,-2 ,-3 ) * ( 1 , 2 , 3 ) \n ( 4 ,-5 , 6 )   ( 5 , 3 , 1 ) \n"
	print my_tensor*other_tensor
	print "MNOZENIE WEKTOROW:\n                 ( 1 ) \n ( 1 , 2 , 3 ) * ( 2 ) \n                 ( 3 ) "
	my_vector = Tensor([[1,2,3]])
	my_other_vector = Tensor([[1],[2],[3]])
	print my_vector*my_other_vector
	print "POTEGA MACIERZY:\n ( 1 , 2 , 3 ) **2 \n (-1 ,-2 ,-3 ) \n ( 4 ,-5 , 6 ) \n"
	print my_tensor**2
	print "DODAWANIE LICZB DO MACIERZY:\n     ( 1 , 2 , 3 ) \n 5 + (-1 ,-2 ,-3 ) \n     ( 4 ,-5 , 6 ) \n"
	print 5+my_tensor

if __name__=="__main__":
	main()
