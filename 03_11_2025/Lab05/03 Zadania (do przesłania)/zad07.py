# 7. Mamy dowolny string np.
dane = 'Python jest najpopularniejszym językiem programowania i słusznie zasłużył na to miano. Jego elastyczność, prostota i potężne zaplecze przyciąga miliony młodych programistów. Wąż rezygnuje z nawiasów klamrowych które to miały otwierać i zamykać bloki kodu oraz średników na końcu każdej linii. Usprawniło to szybkie pisanie i wykluczyło mnóstwo drobnych błędów które były popełniane przez początkujących. Zamiast klamr używa się wcięcia w kodzie (tabulatora ewentualnie czterech znaków spacji) co przekłada się na łatwość nauki. W pythonie praktykuje się pisanie gier komputerowych np: Civilization IV, Metin2, Battlefield i pochodne tej produkcji oraz oprogramowania komputerowego. Świetnym przykładem jest wszystkim dobrze znany Blender program do modelowania i renderowania grafiki 3D czy też Panda3D.'
# Policz ile jest wszystkich niepowtarzających się znaków.

lista = []
lista2 = []
for i in dane:
    if i not in lista:
        lista.append(i)
    else:
        lista2.append(i)
count = 0
for i in dane:
    if i not in lista2:
        count +=1

print(count)