import numpy as np

def read_xyz(file_path):
    """
    Lee un archivo XYZ y devuelve una lista de posiciones de átomos.
    """
    positions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Omitir la primera línea (número de átomos) y la segunda línea (comentario)
        for line in lines[2:]:
            parts = line.split()
            if len(parts) < 4:
                continue
            x, y, z = map(float, parts[1:])
            positions.append((x, y, z))
    return np.array(positions)

def calculate_distances(positions):
    """
    Calcula las distancias entre todos los pares de átomos.
    """
    num_atoms = len(positions)
    distances = np.zeros((num_atoms, num_atoms))
    for i in range(num_atoms):
        for j in range(i + 1, num_atoms):
            dist = np.linalg.norm(positions[i] - positions[j])
            distances[i, j] = dist
            distances[j, i] = dist
            #print(dist)
    return distances

def calculate_coordination_number(distances, cutoff_radius):
    """
    Calcula el número de coordinación basado en un radio de corte.
    """
    num_atoms = distances.shape[0]
    num_neighbors = np.sum(distances < cutoff_radius, axis=1)
    average_coordination_number = np.mean(num_neighbors)
    return average_coordination_number

def main():
    # Ruta al archivo XYZ
    file_path = '39.xyz' #Archivo a leer
    
    # Leer posiciones de átomos
    positions = read_xyz(file_path)
    
    # Calcular distancias entre átomos
    distances = calculate_distances(positions)
    
    # Definir el radio de corte (en la misma unidad que las coordenadas en el archivo)
    cutoff_radius = 2.9316  # mayor distancia en el 40 (2.789) +5%
    
    # Calcular el número de coordinación promedio
    avg_coordination_number = calculate_coordination_number(distances, cutoff_radius)
    #print(distances)
    print(f'Número de coordinación promedio: {avg_coordination_number:.2f}')

if __name__ == "__main__":
    main()

