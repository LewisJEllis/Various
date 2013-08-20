print len([1 for i in range(1,20) for j in range(50) if len(str(i**j)) == j])
