import requests
import json
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta


now = datetime.now()
inicio = now.strftime("%d/%m/%Y %H:%M:%S")
AnoMesString= ''

AnoMes = datetime(2020,3,1)
AnoMesAtual = datetime(2020,4,1)


while AnoMes < AnoMesAtual:

    cont = 0
    with open('C:\Projeto\BolsaFamilia\CodigoMunicipio.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        AnoMesString = AnoMes.strftime('%Y%m')
        
        with open('C:\\Projetos\\Tortoise\\BolsaFamilia\\'+ 'BolsaFamilia_' + AnoMesString + '.csv', mode = 'w', encoding='utf-8', newline='') as csv_file:
            fieldnames = ['DataReferencia', 'CodigoIbgeMunicipio','NomeIBGE','nomeIBGEsemAcento','Pais','UF','Estado','Valor', 'QuantidadeBeneficiados']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for row in csv_reader:
                if line_count == 0:              
                    codigoIbge = (f'{", ".join(row)}')
                    r = requests.get('http://www.transparencia.gov.br/api-de-dados/bolsa-familia-por-municipio?mesAno='+AnoMesString+'&codigoIbge='+codigoIbge+'&pagina=1')
                    data = json.loads(r.text)       
                    if len(str(data)) > 50:            
                        DataReferencia = (data[0]['dataReferencia'])
                        Municipio = (data[0]['municipio'])
                        codigoIbgeMunicipio = (Municipio['codigoIBGE'])
                        nomeIBGE = (Municipio['nomeIBGE'])
                        nomeIBGEsemAcento = (Municipio['nomeIBGEsemAcento'])
                        pais = (Municipio['pais'])
                        uflist = (Municipio['uf'])
                        uf = (uflist['sigla'])
                        ufNome = (uflist['nome'])
                        valor = (data[0]['valor'])
                        quantidadeBeneficiados = (data[0]['quantidadeBeneficiados'])
                        writer.writerow({
                            'DataReferencia': DataReferencia,
                            'CodigoIbgeMunicipio' : codigoIbgeMunicipio, 
                            'NomeIBGE': nomeIBGE, 
                            'nomeIBGEsemAcento': nomeIBGEsemAcento, 
                            'Pais': pais, 
                            'UF': uf, 
                            'Estado': ufNome, 
                            'Valor': int(valor), 
                            'QuantidadeBeneficiados': quantidadeBeneficiados
                            })                         
                        cont = 1 + cont
                        print (str(cont)+ '_'+ AnoMesString + '_' + codigoIbge + '_' + uf + '_' + nomeIBGE + '_' + str(int(valor)))
                        

    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    print('Inicio em:' + inicio)
    print('Final em:' + now)
    AnoMes = AnoMes + relativedelta(months=1)
                        










