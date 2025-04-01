A = int(input())
B = int(input())
C = int(input())

if 90 in [A, B, C]:
    print("Ratvinklig Triangel")

if any(angle > 90 for angle in [A, B, C]):
    print("Trubbig Triangel")

if all(angle < 90 for angle in [A, B, C]):
    print("Spetsig Triangel")
