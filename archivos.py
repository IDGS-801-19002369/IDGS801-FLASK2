#file = open('alumnos.txt', 'r')
#nombres = file.readlines()
#print(nombres)
#file.close()

#file = open('alumnos2.txt', 'w')
#file.write('NUEVO HOLA MUNDO!!!')
#file.close()

file = open('alumnos2.txt', 'a')
file.write('\n' + 'OTRO HOLA MUNDO!!!')
file.close()