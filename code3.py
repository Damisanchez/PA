import math
import numpy as np  # Importar NumPy para la multiplicación de matrices

def matriz_rotacion(theta_x, theta_y, theta_z):
  """
  Calcula la matriz de rotación para un brazo robótico.

  Args:
    theta_x: Ángulo de rotación alrededor del eje X (en grados).
    theta_y: Ángulo de rotación alrededor del eje Y (en grados).
    theta_z: Ángulo de rotación alrededor del eje Z (en grados).

  Returns:
    Matriz de rotación de 3x3 como un array de NumPy.
  """

  # Convertir ángulos a radianes
  theta_x = math.radians(theta_x)
  theta_y = math.radians(theta_y)
  theta_z = math.radians(theta_z)

  # Calcular matrices de rotación individuales usando arrays de NumPy
  Rx = np.array([[1, 0, 0], [0, math.cos(theta_x), -math.sin(theta_x)], [0, math.sin(theta_x), math.cos(theta_x)]])
  Ry = np.array([[math.cos(theta_y), 0, math.sin(theta_y)], [0, 1, 0], [-math.sin(theta_y), 0, math.cos(theta_y)]])
  Rz = np.array([[math.cos(theta_z), -math.sin(theta_z), 0], [math.sin(theta_z), math.cos(theta_z), 0], [0, 0, 1]])

  # Calcular la matriz de rotación final usando la multiplicación de matrices de NumPy
  R = Rz @ Ry @ Rx  # Usar @ para la multiplicación de matrices con NumPy

  return R

# Ejemplo de uso
theta_x = 30
theta_y = 45
theta_z = 60

R = matriz_rotacion(theta_x, theta_y, theta_z)

print("Matriz de rotación:")
print(R)