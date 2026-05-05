def ajustar_motor(nome_motor, posicao, velocidade):
    print(f"--- configurando Hardware ---")
    print(f"motor: {nome_motor}")
    print(f"posição: {posicao}°")
    print(f"velocidade: {velocidade}%")
    print("----------------------------")


ajustar_motor("ombro_direito", 90, 50)
ajustar_motor("joelho_esquerdo", 45, 100)