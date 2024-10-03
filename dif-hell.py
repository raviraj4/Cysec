from random import randint

def diffie_hellman_key_ex():
    P = 101
    G = 9
    
    print(f"P = {P} , G = {G}")
    
    a = randint(1, P-1) # secret no for Walter
    print(f"secret number for Walter: {a}")
    x = pow(G, a , P) # pub key for Walter
    b = randint(1, P-1) # secret no for Jesse
    print(f"secret number for Jesse: {b}")
    y = pow(G, b , P) # pub key for Jesse
    
    ka = pow(y, a, P) # walter's shared key
    kb = pow(x, b, P) # jesse's shared key

    print(f"Shared secret key for \nWalter = {ka}\nJesse = {kb}")
    
    if ka == kb:
        print("Key exchange successfull, both share same key")
    else:
        print("Key exchange failed, keys don't match!")
        
if __name__ == "__main__":
    diffie_hellman_key_ex()
     
    
    
    