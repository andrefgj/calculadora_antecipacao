# Calculadora de antecipação de recebíveis

# Instalação

```
virtualenv -p python3 venv
pip install -r requirements
```

# Uso

```
python calculadora.py
```

Exemplo:

```
$ python calculadora.py 
Insira o valor da venda: 1000
Insira o número de parcelas: 5
Insira a taxa MDR: 1.59
Insira a taxa antecipação: 1.59


Para antecipação de R$ 1000.00 em 5 vezes:

+--------------------+------------------+------------------------+----------+---------------------------------+----------------+
| Número de parcelas | Dias antecipados | Valor bruto da parcela | Taxa MDR | Taxa de antecipação por parcela | Valor deduzido |
+--------------------+------------------+------------------------+----------+---------------------------------+----------------+
|         1          |        30        |         200.0          |   1.59   |               1.59              |     193.69     |
|         2          |        60        |         200.0          |   1.59   |               3.18              |     190.56     |
|         3          |        90        |         200.0          |   1.59   |               4.77              |     187.43     |
|         4          |       120        |         200.0          |   1.59   |               6.36              |     184.30     |
|         5          |       150        |         200.0          |   1.59   |               7.95              |     181.17     |
+--------------------+------------------+------------------------+----------+---------------------------------+----------------+

Valor total antecipado para o cenário é: R$ 937.16

```

## Referências

- https://www.conferecartoes.com.br/blog/taxa-antecipacao-recebiveis