valores_romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def romano_decimal_r(romano, indice=0):
    #Caso base: no quedan más símbolos por procesar
    if indice >= len(romano):
        return 0
 
    valor_actual = valores_romanos[romano[indice]]
 
    #Si hay un símbolo siguiente, se compara para decidir si sumar o restar
    if indice + 1 < len(romano):
        valor_siguiente = valores_romanos[romano[indice + 1]]
 
        if valor_actual < valor_siguiente:
            #Caso de sustracción
            return -valor_actual + romano_decimal_r(romano, indice + 1)
        else:
            #Caso normal: sumamos y avanzamos
            return valor_actual + romano_decimal_r(romano, indice + 1)
 
    #Último símbolo: siempre se suma
    return valor_actual

#Casos de prueba
casos = [
        ("I",       1),
        ("IV",      4),
        ("IX",      9),
        ("XIV",    14),
        ("XL",     40),
        ("XLII",   42),
        ("XC",     90),
        ("XCIX",   99),
        ("CD",    400),
        ("CM",    900),
        ("MCMXC", 1990),
        ("MMXXVI", 2026),
        ("MMMCMXCIX", 3999),
    ]
 
print("=" * 40)
print("  Conversión de Romano → Decimal")
print("=" * 40)
print(f"{'Romano':<14} {'Resultado':>9} {'Esperado':>9} {'OK':>4}")
print("-" * 40)
 
for romano, esperado in casos:
    resultado = romano_decimal_r(romano)
    ok = "✓" if resultado == esperado else "✗"
    print(f"{romano:<14} {resultado:>9} {esperado:>9} {ok:>4}")
 
print("=" * 40)