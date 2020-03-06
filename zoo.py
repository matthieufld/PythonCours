class animal:

	def __init__(self, regime, nombre, nb_pattes, qte_nourriture):
		self.regime = regime
		self.nb_pattes = nb_pattes
		self.qte_nourriture = qte_nourriture
		self.nombre = nombre


class domestique(animal):

	def __init__(self, nb_pattes, mammifere, ani_marin, regime, nombre,qte_nourriture):
		super(). __init__(regime, nombre, qte_nourriture)
		self.nb_pattes = nb_pattes
		self.mammifere = mammifere
		self.marin = marin

	def __str__(self):
		return "{0}, {1}, {2}, {3}, {4}, {5}".format(self.regime, self.qte_nourriture, self.nombre, self.nb_pattes, self.mammifere, self.marin)


class mammifere(animal):

	def __init__(self, regime, qte_nourriture, nombre, nb_pattes, marin, domestique):
		super().__init__(regime, nombre, nb_pattes, qte_nourriture)
		self.nb_pattes = nb_pattes
		self.domestique = domestique
		self.marin = marin
		self.ani_marin = ani_marin

	def __str__(self):
		return "{0}, {1}, {2}, {3}, {4}, {5}".format(self.regime, self.qte_nourriture, self.nombre, self.nb_pattes, self.domestique, self.marin)


class ani_marin(animal):

	def __init__(self, regime, qte_nourriture, nombre, nb_pattes, marin, domestique):
		super().__init__(regime, nombre, domestique, mammifere)
		self.domestique = domestique
		self.mammifere = mammifere

	def __str__(self):
		return "{0}, {1}, {2}, {3}, {4}".format(self.regime, self.qte_nourriture, self.nombre, self.domestique, self.mammifere)
		

if __name__ == "__main__":
	Humain = mammifere("omnivore", "600g", 2, 2, "non", "non")
	Lion = mammifere("carnivore", "3kg", 1, 4, "non", "non")
	Lapin = mammifere("vegetarien", "100g", 7, 4, "oui", "non")
	Mouton = mammifere("vegetarien", "500g", 5, 4, "oui", "non")
	Chien = mammifere("omnivore", "500g", 2, 4, "non", "oui")
	Pieuvre = ani_marin("carnivore", "200g", 1, 0, "non", "oui")

	print (Humain)
	print(Lion)
	print(Lapin)
	print(Mouton)
	print(Chien)
	print(Pieuvre)
