import math

# Noktaların alınması
def get_points():
    points = []
    while True:
        point_str = input("Noktayı girin (x,y) veya çıkmak için 'q' tuşuna basın: ")
        if point_str.lower() == 'q':
            break
        try:
            x, y = map(float, point_str.split(','))
            points.append((x, y))
        except ValueError:
            print("Geçersiz giriş! Lütfen 'x,y' formatında girin.")
    return points

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mesafelerin Hesaplanması
def calculate_distances(points):
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append(distance)
    return distances

# Minimum Mesafenin Bulunması
def find_min_distance(distances):
    return min(distances)

# Noktaları al
points = get_points()

# Mesafeleri hesapla
distances = calculate_distances(points)

# Minimum mesafeyi bul
min_distance = find_min_distance(distances)

print("Minimum Mesafe:", min_distance)
