# TODO здесь писать код
N = int(input("Количество контейнеров: "))
cargo_list = []
for i in range(N):
    cargo_list.append(int(input("Введите вес контейнера: ")))

new_cargo = int(input("Введите вес нового контейнера: "))
cargo_list.sort(reverse=True)
print("Номер, который получит новый контейнер:", cargo_list.index(new_cargo))
