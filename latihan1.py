import math

# Fungsi kuadrat jika hanya satu argumen
a = lambda x: x**2 if isinstance(x, (int, float)) else None

# Fungsi pythagoras jika dua argumen numerik diberikan
b = lambda x, y: math.sqrt(x**2 + y**2) if isinstance(x, (int, float)) and isinstance(y, (int, float)) else None

# Fungsi rata-rata jika minimal dua argumen numerik diberikan
c = lambda *args: sum(args) / len(args) if all(isinstance(arg, (int, float)) for arg in args) and len(args) > 0 else None

# Fungsi menghapus duplikat karakter dari string
d = lambda s: "".join(set(s)) if isinstance(s, str) else None
