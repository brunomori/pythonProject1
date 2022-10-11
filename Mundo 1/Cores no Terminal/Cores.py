def calculoImc (peso, altura):
    seuPeso = float(peso)
    suaAltura = float(altura)
    resultadoImc = seuPeso / suaAltura ** 2
    return resultadoImc

infoPeso = input('Informe seu peso ')
infoAltura = input('Informe sua altura ')

seuImc = calculoImc(infoPeso, infoAltura)

resp = "S"
while resp in 'Ss':
    resp = str(input('Deseja Verificar outro paciente? [S/N] ')).upper().strip()[0]

    if seuImc <= 19.1:
        print('Seu IMC é: {} Seu paciente está com baixo peso '.format("%.1f"%(seuImc)))

    if seuImc >= 19.1 and seuImc <= 25.8:
        print('Seu IMC é: {} Seu paciente está com peso ideal '.format("%.1f"%(seuImc)))

    if seuImc >= 25.8 and seuImc <= 27.3:
        print('Seu IMC é: {} Seu paciente está um pouco acima do peso '.format("%.1f"%(seuImc)))

    if seuImc >= 27.3 and seuImc <= 32.3:
            print('Seu IMC é: {} Seu paciente está muito acima do peso '.format("%.1f"%(seuImc)))

    if seuImc >= 32.3:
        print('Seu IMC é: {} Seu paciente está com obesidade '.format("%.1f"%(seuImc)))