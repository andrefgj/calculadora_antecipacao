from prettytable import PrettyTable
import argparse

def main():
    # Create the parser
    my_parser = argparse.ArgumentParser(description='Caxlculadora de antecipação de recebíveis')

    # Add the arguments
    my_parser.add_argument('--valor-da-venda',        dest="valor_da_venda",      type=float,   help='valor da venda')
    my_parser.add_argument('--numero-de-parcelas',    dest="numero_de_parcelas",  type=int,   help='numero de parcelas')
    my_parser.add_argument('--taxa-de-mdr',           dest="taxa_de_mdr",         type=float, help='taxa de mdr')
    my_parser.add_argument('--taxa-antecipacao',      dest="taxa_antecipacao",    type=float, help='taxa de antecipação')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    t = PrettyTable(["Número de parcelas", "Dias antecipados", "Valor bruto da parcela", "Taxa MDR", "Taxa de antecipação por parcela", "Valor deduzido"])

    valor_da_venda = None if args.valor_da_venda is None else args.valor_da_venda
    numero_de_parcelas = None if args.numero_de_parcelas is None else args.numero_de_parcelas
    taxa_de_mdr = None if args.taxa_de_mdr is None else args.taxa_de_mdr
    taxa_antecipacao = None if args.taxa_antecipacao is None else args.taxa_antecipacao


    if (valor_da_venda) is None:
        valor_da_venda = float(input('Insira o valor da venda: '))

    if (numero_de_parcelas) is None:
        numero_de_parcelas = int(input('Insira o número de parcelas: '))

    if (taxa_de_mdr) is None:
        taxa_de_mdr = float(input('Insira a taxa MDR: '))

    if (taxa_antecipacao) is None:
        taxa_antecipacao = float(input('Insira a taxa antecipação: '))

    valor_parcela_com_taxa_mdr = (valor_da_venda - (valor_da_venda / 100  * taxa_de_mdr)) / numero_de_parcelas
    valor_bruto_parcela = valor_da_venda / numero_de_parcelas

    valor_total_antecipado = 0

    for x in range(numero_de_parcelas):
        
        valor_deduzido = valor_parcela_com_taxa_mdr - (valor_parcela_com_taxa_mdr / 100 * (taxa_antecipacao * (x + 1)))
        t.add_row([x+1, 30 * (x + 1), "%.2f" % round(valor_bruto_parcela, 2), "%.2f" % round((taxa_de_mdr), 2) + " %", "%.2f" % round((taxa_antecipacao * (x + 1)),2) + " %", "%.2f" % round(valor_deduzido, 2)])
        valor_total_antecipado = valor_total_antecipado + valor_deduzido

    print(f"""
    Para antecipação de R$ {'%.2f' % round(valor_da_venda)} em {numero_de_parcelas} vezes:

    {t}

    Valor total antecipado para o cenário é: R$ {'%.2f' % round(valor_total_antecipado, 2)}

    """)


if __name__ == "__main__":
    main()