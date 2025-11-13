def main():
    print("**********************************")
    print("*      CALCULADORA BÁSICA       *")
    print("**********************************")
    print()
    print("Puedes usar estas operaciones:")
    print("+ para sumar")
    print("- para restar") 
    print("* para multiplicar")
    print("/ para dividir")
    print("** para potencia")
    print("% para módulo")
    print()
    print("Escribe 'salir' para terminar")
    print()
    
    while True:
        num1_texto = input("Dime el primer número: ")
        
        if num1_texto == "salir":
            print("¡Adiós! Gracias por usar la calculadora")
            break
        
        try:
            num1 = float(num1_texto)
        except:
            print("¡Eso no es un número válido! Intenta otra vez")
            print()
            continue
        
        num2_texto = input("Dime el segundo número: ")
        
        try:
            num2 = float(num2_texto)
        except:
            print("¡Eso no es un número válido! Intenta otra vez")
            print()
            continue
        
        operacion = input("¿Qué operación quieres hacer? (+, -, *, /, **, %): ")
        
        resultado = None
        error = False
        
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                print("¡ERROR! No se puede dividir entre cero")
                error = True
            else:
                resultado = num1 / num2
        elif operacion == "**":
            resultado = num1 ** num2
        elif operacion == "%":
            if num2 == 0:
                print("¡ERROR! No se puede hacer módulo con cero")
                error = True
            else:
                resultado = num1 % num2
        else:
            print("¡OPERACIÓN NO VÁLIDA! Usa solo: +, -, *, /, **, %")
            error = True
        
        if not error:
            print(f"RESULTADO: {num1} {operacion} {num2} = {resultado}")
        
        print()  # Línea en blanco para separar

print("=== INFORMACIÓN DE LA CALCULADORA ===")
print("Esta calculadora puede:")
print("- Sumar números")
print("- Restar números") 
print("- Multiplicar números")
print("- Dividir números")
print("- Calcular potencias")
print("- Calcular módulo")
print("=====================================")
print()

if __name__ == "__main__":
    main()