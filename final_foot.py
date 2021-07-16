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
	standard = 0.185
	
	print(total,'\n','主胜',round(z3,3),'平',round(p1,3),'客胜',round(f0,3))
	print(total1,'\n','主胜',round(z13,3),'平',round(p11,3),'客胜',round(f10,3))
	if round(zhusheng1,3)- round(zhusheng,3) < 0:
		print('主胜降盘',round((zhusheng1-zhusheng),3))
	if round(ping1,3)-round(ping,3) < 0:
		print('平降盘',round((ping1-ping),3))
	if round(fu1,3)- round(fu,3) < 0:
		print('客胜降盘',round((fu1-fu),3))
		
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
		print('让球首赔和中赔不错的选择！最好是平')
	
	# if total > total_flag :
		# if z3 < standard and zhusheng < ping and zhusheng < fu:
			# if zhusheng < ping and zhusheng < fu:
				# zhusheng1 = float(input('输入变化后主胜：'))
				# if zhusheng1/zhusheng >1.5:
					# print("小心变化")
			# print(3)
			# continue
		# if p1 < standard and zhusheng > ping and ping < fu:
			# if  ping<zhusheng and ping < fu:
				# ping1 = float(input ('输入变化后平：'))
				# if ping1/ping > 1.5:
					# print("小心变化")
			# print(1)
			# continue
		# if f0 < standard and  fu < ping and zhusheng < fu:
			# if  fu < zhusheng and fu < ping:		
				# fu1 = float(input ('输入变化后负：'))
				# if	fu1/fu > 1.5:
					# print("小心变化")
			# print(0)
			# continue
		
