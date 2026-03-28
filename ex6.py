Idade = int (input("Digite sua idade:"))

if Idade < 18:
    print("Menor de idade")
elif Idade > 18 and Idade < 60:
    print("Maior de idade")
elif Idade >= 60:
    print("idoso")


nota1 = float(input("Digite a primeira nota do aluno:"))
nota2 = float(input("Digite a segunda nota do aluno:"))
nota3 = float(input("Digite a terceira nota do aluno:"))

media = (nota1 + nota2 + nota3) / 3 

if media >= 6.0:
 print(f"{media:.2f}" , "Aprovado")
else:
   print("Reprovado")
