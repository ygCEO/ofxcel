#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import datetime
from ofxparse import OfxParser
import pandas as pd

def parse_ofx(file_path):
    """
    Parseia um arquivo OFX e retorna o objeto de transações.
    
    Args:
        file_path (str): Caminho para o arquivo OFX
        
    Returns:
        ofxparse.Statement: Objeto com as transações do arquivo OFX
    """
    try:
        with open(file_path, 'rb') as ofx_file:
            ofx = OfxParser.parse(ofx_file)
            return ofx.account.statement
    except Exception as e:
        print(f"Erro ao processar o arquivo OFX: {e}")
        return None

def convert_to_dataframe(statement):
    """
    Converte as transações de um statement OFX para um DataFrame do pandas.
    
    Args:
        statement (ofxparse.Statement): Statement com as transações
        
    Returns:
        pandas.DataFrame: DataFrame com as transações formatadas
    """
    if not statement or not statement.transactions:
        return pd.DataFrame()
    
    transactions = []
    
    for transaction in statement.transactions:
        trans_dict = {
            'data': transaction.date,
            'tipo': transaction.type,
            'valor': transaction.amount,
            'id': transaction.id,
            'descrição': transaction.payee,
            'memo': transaction.memo
        }
        transactions.append(trans_dict)
    
    df = pd.DataFrame(transactions)
    
    # Ordenar por data
    df = df.sort_values('data')
    
    return df

def save_to_excel(df, output_path):
    """
    Salva o DataFrame em um arquivo Excel.
    
    Args:
        df (pandas.DataFrame): DataFrame com os dados
        output_path (str): Caminho para salvar o arquivo Excel
    """
    try:
        writer = pd.ExcelWriter(output_path, engine='openpyxl')
        df.to_excel(writer, index=False, sheet_name='Transações')
        
        # Ajustar largura das colunas
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            writer.sheets['Transações'].column_dimensions[chr(65 + col_idx)].width = column_width + 2
        
        writer.close()
        return True
    except Exception as e:
        print(f"Erro ao salvar arquivo Excel: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Conversor de OFX para Excel')
    parser.add_argument('input', help='Arquivo OFX ou diretório contendo arquivos OFX')
    parser.add_argument('-o', '--output', help='Arquivo Excel de saída ou diretório')
    
    args = parser.parse_args()
    
    # Verificar se o caminho de entrada é um arquivo ou diretório
    if os.path.isfile(args.input):
        ofx_files = [args.input]
    elif os.path.isdir(args.input):
        ofx_files = [os.path.join(args.input, f) for f in os.listdir(args.input) if f.lower().endswith('.ofx')]
    else:
        print(f"Erro: '{args.input}' não é um arquivo ou diretório válido.")
        return
    
    if not ofx_files:
        print("Nenhum arquivo OFX encontrado.")
        return
    
    for ofx_file in ofx_files:
        # Determinar nome de arquivo de saída
        if args.output:
            if os.path.isdir(args.output):
                base_name = os.path.basename(ofx_file).rsplit('.', 1)[0]
                output_file = os.path.join(args.output, f"{base_name}.xlsx")
            else:
                output_file = args.output
        else:
            base_name = os.path.basename(ofx_file).rsplit('.', 1)[0]
            output_file = f"{base_name}.xlsx"
        
        print(f"Processando: {ofx_file}")
        
        # Extrair dados do OFX
        statement = parse_ofx(ofx_file)
        if statement:
            # Converter para DataFrame
            df = convert_to_dataframe(statement)
            
            if not df.empty:
                # Salvar como Excel
                if save_to_excel(df, output_file):
                    print(f"Arquivo Excel salvo com sucesso: {output_file}")
            else:
                print("Nenhuma transação encontrada no arquivo.")
    
    print("Processamento concluído.")

if __name__ == "__main__":
    main()