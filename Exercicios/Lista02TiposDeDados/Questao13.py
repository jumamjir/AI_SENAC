#13. Solicite um email e exiba o domínio do email após o @.

email = input("Digite seu email:")

pararApos = "@"

print("O email original é: " + email)

dps = email.split(pararApos,1)

print("Apenas o domínio do endereço de email digitado é:" , dps[1])

