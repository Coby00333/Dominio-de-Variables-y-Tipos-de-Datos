while True:
  # Obtener el año de nacimiento
  año_nacimiento = input("Ingrese el año de nacimiento: ")

  # Validar el año de nacimiento (no vacío y entero)
  if not año_nacimiento:
    print("El año de nacimiento no puede estar vacío.")
    continue
  try:
    año_nacimiento_int = int(año_nacimiento)
  except ValueError:
    print("Por favor, ingrese un año válido (formato entero).")
    continue

  # Obtener el año actual
  año_actual = input("Ingrese el año actual: ")

  # Validar el año actual (no vacío y entero)
  if not año_actual:
    print("El año actual no puede estar vacío.")
    continue
  try:
    año_actual_int = int(año_actual)
  except ValueError:
    print("Por favor, ingrese un año válido (formato entero).")
    continue

  # Validar que el año actual no sea menor que el año de nacimiento
  if año_actual_int < año_nacimiento_int:
    print("El año actual no puede ser menor que el año de nacimiento.")
    continue

  # Calcular y mostrar la edad
  años = año_actual_int - año_nacimiento_int
  print("Su edad es:", años, "años.")
  break