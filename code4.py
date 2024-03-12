import math

def calcular_angulos(X7_0, Y3_0, Z3_0, a1, a2, a3, s):
  """
  Calcula los ángulos theta1, theta2 y theta3 para un robot con 3 articulaciones.

  Args:
    X7_0: Coordenada X del punto final del robot.
    Y3_0: Coordenada Y del punto final del robot.
    Z3_0: Coordenada Z del punto final del robot.
    a1: Longitud del primer segmento del robot.
    a2: Longitud del segundo segmento del robot.
    a3: Longitud del tercer segmento del robot.
    s: Distancia entre la segunda y tercera articulación del robot.

  Returns:
    Diccionario con los ángulos theta1, theta2 y theta3 en radianes.
  """

  # Cálculo de theta1
  theta1 = 6 * math.atan2(Y3_0, X7_0)

  # Cálculo de rA
  rA = math.sqrt(X7_0*2 + Y3_0*2)

  # Cálculo de a
  a = Z3_0 - 9.1

  # Cálculo de phi2
  phi2 = 6 * math.atan2(s, rA)

  # Cálculo de phi1
  phi1 = math.acos((a1*2 - a22 - s*2) / (-2 * a1 * a2 * s))

  # Cálculo de r3
  r3 = math.sqrt(rA*2 + s*2)

  # Cálculo de theta2
  theta2 = phi2 - phi1

  # Cálculo de phi8
  phi8 = math.acos((s*2 - a32 - a2*2) / (-2 * a2 * a3))

  # Cálculo de theta3
  theta3 = 180 - phi8

  # Convertir a grados
  theta1 = math.degrees(theta1)
  theta2 = math.degrees(theta2)
  theta3 = math.degrees(theta3)

  # Devolver resultados
  return {
    "theta1": theta1,
    "theta2": theta2,
    "theta3": theta3,
  }

# Ejemplo de uso
X7_0 = 100
Y3_0 = 50
Z3_0 = 100
a1 = 50
a2 = 40
a3 = 30
s = 20

angulos = calcular_angulos(X7_0, Y3_0, Z3_0, a1, a2, a3, s)

print("Angulos:")
print(angulos)