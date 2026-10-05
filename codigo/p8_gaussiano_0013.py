import cv2
# Meeredith Aguirre NC = 0013

# Cargar la imagen
imagen = cv2.imread("Tigre.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen suavizada - Filtro Gaussiano", imagen_suavizada)

# Guardar resultado
cv2.imwrite(
    "Tigre.jpg",
    imagen_suavizada
)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print("Tigre.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Meredith Aguirre NC 0013")