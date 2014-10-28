table = {'Ru': 101.07, 'Re': 186.21, 'Rg': 280.16, 'Ra': 226.03, 'Rb': 85.468, 'Rn': 222.02, 'Rh': 102.91, 'Rj': 265.12, 'Be': 9.0122, 'Ba': 137.33, 'Bh': 270.0, 'Bi': 208.98, 'Bk': 247.07, 'Br': 79.904, 'H': 1.008, 'P': 30.974, 'Os': 190.23, 'Es': 252.08, 'Hg': 200.59, 'Ge': 72.63, 'Gd': 157.25, 'Ga': 69.723, 'Pr': 140.91, 'Pt': 195.08, 'Pu': 244.06, 'C': 12.011, 'Pb': 207.2, 'Pa': 231.04, 'Pd': 106.42, 'Po': 208.98, 'Pm': 144.91, 'Hs': 277.15, 'Uup': 288.19, 'Uus': 294.0, 'Uuo': 294.0, 'Ho': 164.93, 'Hf': 178.49, 'Mo': 95.96, 'He': 4.0026, 'Md': 258.1, 'Mg': 24.305, 'K': 39.098, 'Mn': 54.938, 'O': 15.999, 'Mt': 276.15, 'S': 32.06, 'W': 183.84, 'Zn': 65.48, 'Eu': 151.96, 'Zr': 91.224, 'Er': 167.26, 'Ni': 58.693, 'No': 259.1, 'Na': 22.99, 'Nb': 92.906, 'Nd': 144.24, 'Ne': 20.18, 'Np': 237.05, 'Fr': 223.02, 'Fe': 55.845, 'Fl': 289.19, 'Fm': 257.1, 'B': 10.81, 'F': 18.998, 'Sr': 87.62, 'N': 14.007, 'Kr': 83.798, 'Si': 28.085, 'Sn': 118.71, 'Sm': 150.36, 'V': 50.942, 'Sc': 44.956, 'Sb': 121.76, 'Sg': 271.13, 'Se': 78.96, 'Co': 58.933, 'Cn': 285.17, 'Cm': 247.07, 'Cl': 35.45, 'Ca': 40.078, 'Cf': 251.08, 'Ce': 140.12, 'Xe': 131.29, 'Cs': 132.91, 'Cr': 51.996, 'Cu': 63.546, 'Lm': 168.93, 'Li': 6.94, 'Lv': 293.0, 'Lu': 174.97, 'Lr': 262.11, 'Th': 232.04, 'Ti': 204.38, 'Te': 127.6, 'Tb': 158.93, 'Tc': 97.91, 'Ta': 180.95, 'Yb': 173.05, 'Db': 268.13, 'Dy': 162.5, 'Ds': 281.16, 'I': 126.9, 'In': 114.82, 'U': 238.03, 'Y': 88.906, 'Ac': 227.03, 'Ag': 107.87, 'Ir': 192.22, 'Am': 243.06, 'Al': 26.982, 'As': 74.922, 'Ar': 39.948, 'Au': 196.97, 'At': 209.99, 'Uut': 284.18}



formula = raw_input("Enter formula: ")
mass = 0
found = True

while found == True and len(formula) > 0:
	for element in table.keys():
		elemIndex = formula.find(element)
		if(elemIndex != -1):
			found = True
			if len(formula) > len(element):
				numIndex = elemIndex + len(element)
				numElement = formula[numIndex]
				
				if(ord(numElement) > 48 and ord(numElement) < 58):
					numElement = float(numElement)
				else:
					numElement = 1.0
				
				if(numIndex+1 < len(formula)):
					numIndex = numIndex + 1
					while numIndex < len(formula) and ord(formula[numIndex]) > 48 and ord(formula[numIndex]) < 58:
						numElement = numElement * 10 + float(formula[numIndex])
						numIndex +=1
				#this leaves the index at one place beyond the number (i.e. C6H12O2 has an index on O, rendering the old code below as
				# it was one created for the index being on the last number after the element)
			else:
				numElement = 1.0
			print element
			print numElement
			mass += numElement * table[element]
			formula = formula[:elemIndex] + formula[numIndex:]
			print formula
		else:
			found = False
print mass

