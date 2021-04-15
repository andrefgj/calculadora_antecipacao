# Calculadora de antecipação de recebíveis

## Requisitos

- `python3`: https://www.python.org/downloads/

## Instalação

```
pip3 install virtualenv
virtualenv -p python3 venv
pip3 install -r requirements.txt
python setup sdist
```

## Uso

```
calcrec
```

Exemplo:

```
$ calcrec 
Insira o valor da venda: 1000
Insira o número de parcelas: 5
Insira a taxa MDR: 1.59
Insira a taxa antecipação: 1.59


Para antecipação de R$ 1000.00 em 5 vezes:

+--------------------+------------------+------------------------+----------+---------------------------------+----------------+
| Número de parcelas | Dias antecipados | Valor bruto da parcela | Taxa MDR | Taxa de antecipação por parcela | Valor deduzido |
+--------------------+------------------+------------------------+----------+---------------------------------+----------------+
|         1          |        30        |         200.00         |  1.59 %  |              1.59 %             |     193.69     |
|         2          |        60        |         200.00         |  1.59 %  |              3.18 %             |     190.56     |
|         3          |        90        |         200.00         |  1.59 %  |              4.77 %             |     187.43     |
|         4          |       120        |         200.00         |  1.59 %  |              6.36 %             |     184.30     |
|         5          |       150        |         200.00         |  1.59 %  |              7.95 %             |     181.17     |
+--------------------+------------------+------------------------+----------+---------------------------------+----------------+

Valor total antecipado para o cenário é: R$ 937.16

```

## Referências

- https://www.conferecartoes.com.br/blog/taxa-antecipacao-recebiveis