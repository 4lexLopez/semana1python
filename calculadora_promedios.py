def main():
  print("*CALCULADOR DE PROMEDIO DE MATERIAS*\n")
  notas, materias = ingresar_calificaciones()
  
  print(f"\nMaterias y sus calificaciones: ")
  for i in len(materias):
    print(f"\nMateria: {materias[i]}, Nota: {notas[i]}")
  
  print(f"\nEl promedio general de calificaciones es: {calcular_promedio(notas):.2f}")
  
  aprobadas, reprobadas = determinar_estado(notas)
  print("\nlas materias aprobadas fueron:")
  if(len(aprobadas) > 0):
    for i in aprobadas:
      print(f"{materias[i]}\n")
  else:
    print("\nNinguna")      
  print("\nlas materias reprobadas fueron:")
  if(len(reprobadas) > 0):
    for i in reprobadas:
      print(f"{materias[i]}\n")
  else:
    print("\nNinguna")
  
  alta, baja = encontrar_extremos(notas)
  print(f"\nla materia con la mejor calificacion fue: {materias[alta]}")
  print(f"\nla materia con la peor calificacion fue: {materias[baja]}")
  
def ingresar_calificaciones():
  materias = list()
  notas = list()
  while(True):
    nombre_materia = input("\nIngrese nombre de la materia: ")
    if not nombre_materia:
      print("\nNombre de materia invalido.\n")
    else:
      materias.append(nombre_materia)
      while(True):
        print(f"\nIngrese la calificacion de la materia {nombre_materia}: ")
        calificacion_materia = input()
        if(calificacion_materia.isnumeric()):
          nota = int(calificacion_materia)
          if nota >= 0 & nota <= 10: 
            notas.append(nota)
            break
        else:
          print("\nCalificion invalida\n")
          
    while(True):
        print("\nDesea agregar mas materias?: S/N")
        opcion = input()
        if (opcion == 'S' or opcion == 's'):
            break
        if (opcion == 'N' or opcion == 'n'):
            return notas, materias
        else:
            print("\nOpcion invalida\n")

def calcular_promedio(calificaciones: list):
  return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones: list, umbral: float = 5.0):
  return [i for i, nota in enumerate(calificaciones) if nota >= umbral], [i for i, nota in enumerate(calificaciones) if nota < umbral]
  
def encontrar_extremos(calificaciones: list):
  return calificaciones.index(max(calificaciones)), calificaciones.index(min(calificaciones))

if __name__ == "__main__":
  main()
