import random

minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "0123456789"

simbolos = "@$&#/)!?'*'"

nose = minus + mayus + numeros + simbolos

nosex2 = 10
contra = "".join(random.sample(nose, nosex2))

print("tu contraseña es:", contra)
