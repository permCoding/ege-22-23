def f(x,y,z):  # (x ≡ z ) ∨ (x → (y ∧ z))
    return (x==z) or (x <= (y and z))


for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if not(f(x,y,z)):
                print(y,z,x)
# решаем простой перестановкой 
# пока не совпадут все строки в таблице
