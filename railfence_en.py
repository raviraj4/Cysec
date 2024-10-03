def rail_fence_en(plain, rails):
    rail = [['' for _ in range(len(plain))] for _ in range(rails)]

    direction_down = False
    row, col = 0, 0

    for char in plain:
        rail[row][col] = char

        col += 1

        if row == 0 or row == rails - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1

    en_text = ''.join([rail[row][col] for row in range(rails) for col in range(len(plain)) if rail[row][col] != ''])
    return en_text


plain = "ATTACKLEB"

n_rails = 4
cipher = rail_fence_en(plain, n_rails)

print(f"Plain: {plain} \nCipher: {cipher}")

