while True:
	zhusheng = float(input('输入主胜：'))
	ping = float(input ('输入平：'))
	fu = float(input ('输入负：'))
	
	zhusheng1 = float(input('输入变化后主胜：'))
	ping1 = float(input ('输入变化后平：'))
	fu1 = float(input ('输入变化后负：'))
	
	total = zhusheng+ping+fu
	z3 = zhusheng/total
	p1 = ping/total
	f0 = fu/total
	
	total1 = zhusheng1+ping1+fu1
	z13 = zhusheng1/total1
	p11 = ping1/total1
	f10 = fu1/total1
	
	total_flag = 36.7
	standard = 0.19
	
	print(total,'\n','主胜',z3,'平',p1,'客胜',f0)
	print(total1,'\n','主胜',z13,'平',p11,'客胜',f10)
	
	if total > total_flag :
		if ( zhusheng < ping and zhusheng < fu) and (zhusheng1 < ping1 and zhusheng1 < fu1):
			if z3 < standard:
				if zhusheng1/zhusheng >1.5:
					print("小心变化")
				print(3)
				continue
		if (ping < zhusheng and ping < fu) and (ping1 < zhusheng1 and ping1 < fu1):
			if p1 < standard :
				if ping1/ping > 1.5:
					print("小心变化")
				print(1)
				continue
		if (fu < zhusheng and fu < ping) and (fu1 < zhusheng1 and fu1 < ping1):
			if f0 < standard :
				if	fu1/fu > 1.5:
					print("小心变化")
			print(0)
			continue
		else:
			print('我是因为standard')
			print('让球首赔和中赔不错的选择！')
	else:
		print('我是因为total')
		print('让球首赔和中赔不错的选择！')
