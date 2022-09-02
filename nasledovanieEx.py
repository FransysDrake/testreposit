class CarsClass():
	"""Класс автомобилей"""
	def __init__(self, brand, model, year, probeg):
		"""Инициализация атрибутов"""
		self.brand = brand
		self.model = model
		self.year = year
		self.probeg = int(probeg)
	
	def showCar(self):
		"""Показать информацию о машине"""
		print(f'{self.brand}, {self.model}, {self.year} год, {self.probeg} km')

	def drowCar(self, km):
		""" Метод поездки авто """ 
		self.probeg = self.probeg + km

		
# f_car = CarsClass('audi', 'q3', '2010', 99000)
s_car = CarsClass('Lada', 'Granta', '2020', 10)
s_car.showCar()
s_car.drowCar(100)
s_car.showCar()


class ElectroCar(CarsClass):
	"""Класс электрокаров, инициализация атрибутов"""
	def __init__(self, brand, model, year, probeg):
		super().__init__(brand, model, year, probeg)
		self.battery = 100 #потом удалить

	def description_battery(self):
		'''Выводит информацию о батарее'''
		print('Этот автомобиль имеет мощьность ' + str(self.battery) + ' %')

	def showCar(self):
		"""Показать информацию о машине"""
		print(f'{self.brand}, {self.model}')

tesla = ElectroCar('Tesls', 'T', '2017', 10000)
tesla.showCar()
tesla.description_battery()
s_car.description_battery()
tesla.showCar()
s_car.showCar()


class Battery():
	"""Класс батареи"""
	def __init__(self, battery = 100):
		self.battery = battery
	
	def description_battery(self):
		'''Выводит информацию о батарее'''
		print('Этот автомобиль имеет мощьность ' + str(self.battery) + ' %')


class ElectroCar(CarsClass):
	"""Класс электрокаров"""
	def __init__(self, brand, model, year, probeg):
		super().__init__(brand, model, year, probeg)
		self.battery = Battery()

	def showCar(self):
		"""Показать информацию о машине"""
		print(f'{self.brand}, {self.model}')

akum = Battery()