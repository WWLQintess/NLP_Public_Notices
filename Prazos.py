def data_tradutor(texto):
   str_resultante = str(texto)[0:2]
   str_resultante = str_resultante.strip(' ')
   dia = 0
   ano = 0
   offset = 0
   if str_resultante.isdigit():
      dia = int(str(texto)[0:2])
   idx = str(texto).find('de janeiro de')
   mes = 0
   if idx != -1:
      mes = 1
      offset = idx + 14
   else:
      idx = str(texto).find('de fevereiro de')
      if idx != -1:
         mes = 2
         offset = idx + 16
      else:
         idx = str(texto).find('de março de')
         if idx != -1:
            mes = 3
            offset = idx + 12
         else:
            idx = str(texto).find('de abril de')
            if idx != -1:
               mes = 4
               offset = idx + 12
            else:
               idx = str(texto).find('de maio de')
               if idx != -1:
                  mes = 5
                  offset = idx + 11
               else:
                  idx = str(texto).find('de junho de')
                  if idx != -1:
                     mes = 6
                     offset = idx + 12
                  else:
                     idx = str(texto).find('de julho de')
                     if idx != -1:
                        mes = 7
                        offset = idx + 12
                     else:
                        idx = str(texto).find('de agosto de')
                        if idx != -1:
                           mes = 8
                           offset = idx + 13
                        else:
                           idx = str(texto).find('de setembro de')
                           if idx != -1:
                              mes = 9
                              offset = idx + 15
                           else:
                              idx = str(texto).find('de outubro de')
                              if idx != -1:
                                 mes = 10
                                 offset = idx + 14
                              else:
                                 idx = str(texto).find('de novembro de')
                                 if idx != -1:
                                    mes = 11
                                    offset = idx + 15
                                 else:
                                    idx = str(texto).find('de dezembro de')
                                    if idx != -1:
                                       mes = 12
                                       offset = idx + 15
                                    else:
                                          str_resultante = str(texto)[0:10]
                                          str_resultante = str_resultante.strip(' ')
                                          from datetime import datetime as dt
                                          from datetime import date
                                          data = dt.strptime(str_resultante, '%d/%m/%Y')
                                          dia = int(data.strftime('%d'))
                                          mes = int(data.strftime('%m'))
                                          ano = int(data.strftime('%Y'))
                                          offset = 11
   if dia != 0:
      if ano == 0:
         if str(texto)[offset:offset + 4].isdigit():
            ano = int(str(texto)[offset:offset + 4])
   return dia, mes, ano, offset

def prazos(texto, data_publicacao):
    listaPrazos = []
    listaOffsets = []
    listaDatas = []
    dia = 0
    mes = 0
    ano = 0
    idx = str(texto).find('o prazo de até')
    if idx != -1:
        str_resultante = str(texto)[idx + 15:idx + 17]
        if str_resultante.isdigit():
            listaPrazos.append(str(texto)[idx + 15:idx + 17])
        else:
            listaPrazos.append(np.nan)
        listaOffsets.append(idx + 15)
        listaDatas.append('')
    else:
        idx = str(texto).find('o prazo de')
        if idx != -1:
            str_resultante = str(texto)[idx + 11:idx + 13]
            if str_resultante.isdigit():
                listaPrazos.append(str(texto)[idx + 11:idx + 13])
            else:
                listaPrazos.append(np.nan)    
            listaOffsets.append(idx + 11)
            listaDatas.append('')
        else:
            idx = str(texto).find('no prazo máximo de')
            if idx != -1:
                str_resultante = str(texto)[idx + 19:idx + 21]
                if str_resultante.isdigit():
                    listaPrazos.append(str(texto)[idx + 19:idx + 21])
                else:
                    listaPrazos.append(np.nan)    
                listaOffsets.append(idx + 19)
                listaDatas.append('')
            else:
                idx = str(texto).find('o prazo máximo de')
                if idx != -1:
                    str_resultante = str(texto)[idx + 18:idx + 20]
                    if str_resultante.isdigit():
                        listaPrazos.append(str(texto)[idx + 18:idx + 20])
                    else:
                        listaPrazos.append(np.nan)    
                    listaOffsets.append(idx + 18)
                    listaDatas.append('')
                else:
                    idx = str(texto).find('com prazo de')
                    if idx != -1:
                        str_resultante = str(texto)[idx + 13:idx + 15]
                        if str_resultante.isdigit():
                            listaPrazos.append(str(texto)[idx + 13:idx + 15])
                        else:
                            listaPrazos.append(np.nan)    
                        listaOffsets.append(idx + 13)
                        listaDatas.append('')
                    else:
                        idx = str(texto).find('até às 23 horas e 59 minutos do décimo dia')
                        if idx != -1:
                                listaPrazos.append('10')
                                listaOffsets.append(idx - 2)
                                listaDatas.append('')
                        else:
                            idx = str(texto).find('até às 23 horas e 59 minutos do dia')
                            if idx != -1:
                                listaPrazos.append(-1)
                                listaOffsets.append(idx + 36)
                                listaDatas.append(str(texto)[idx + 36:idx + 36 + 23])
                            else:
                                idx = str(texto).find('até às 23h59min do dia')
                                if idx != -1:
                                    listaPrazos.append(-1)
                                    listaOffsets.append(idx + 23)
                                    listaDatas.append(str(texto)[idx + 23:idx + 23 + 23])
                                else:                           
                                    idx = str(texto).find('até às 24hs do dia')
                                    if idx != -1:
                                        listaPrazos.append(-1)
                                        listaOffsets.append(idx + 19)
                                        listaDatas.append(str(texto)[idx + 19:idx + 19 + 23])
                                    else:
                                        idx = str(texto).find('novo prazo para apresentação') 
                                        if idx != -1:
                                            idx1 = str(texto).find('manifestações deverão ser encaminhadas até o dia')
                                            if idx1 != -1:
                                                listaPrazos.append(-1)
                                                listaOffsets.append(idx1 + 49)
                                                listaDatas.append(str(texto)[idx1 + 49:idx1 + 49 + 23])
                                            else:
                                                idx1 = str(texto).find('manifestações deverão ser encaminhadas até a data de')
                                                if idx1 != -1:
                                                    listaPrazos.append(-1)
                                                    listaOffsets.append(idx1 + 53)
                                                    listaDatas.append(str(texto)[idx1 + 53:idx1 + 53 + 23])                                    
                                                else:
                                                    idx1 = str(texto).find('manifestações deverão ser encaminhadas até a data')
                                                    if idx1 != -1:
                                                        listaPrazos.append(-1)
                                                        listaOffsets.append(idx1 + 50)
                                                        listaDatas.append(str(texto)[idx1 + 50:idx1 + 50 + 23])
                                                    else:
                                                        idx1 = str(texto).find('manifestações deverão ser encaminhadas até')
                                                        if idx1 != -1:
                                                            listaPrazos.append(-1)
                                                            listaOffsets.append(idx1 + 43)
                                                            listaDatas.append(str(texto)[idx1 + 43:idx1 + 43 + 23])
                                                        else:
                                                            idx1 = str(texto).find('nova data limite para recebimento das manifestações será dia')
                                                            if idx1 != -1:
                                                                listaPrazos.append(-1)
                                                                listaOffsets.append(idx1 + 61)
                                                                listaDatas.append(str(texto)[idx1 + 61:idx1 + 61 + 23])
                                                            else:
                                                                idx1 = str(texto).find('prazo para apresentação de manifestações fica prorrogado por')
                                                                if idx1 != -1:
                                                                    str_resultante = str(texto)[idx1 + 61:idx1 + 63]
                                                                    if str_resultante.isdigit():
                                                                        listaPrazos.append(str(texto)[idx1 + 61:idx1 + 63])
                                                                    else:
                                                                        listaPrazos.append(np.nan) 
                                                                    listaOffsets.append(idx1 + 61)
                                                                    listaDatas.append('')
                                                                else:
                                                                    listaPrazos.append(np.nan)
                                                                    listaOffsets.append(idx)
                                                                    listaDatas.append('')                            
                                        else:
                                            idx = str(texto).find('Consulta Pública permanecerá disponível por')
                                            if idx != -1:
                                                str_resultante = str(texto)[idx + 44:idx + 46]
                                                if str_resultante.isdigit():
                                                    listaPrazos.append(str(texto)[idx + 44:idx + 46])
                                                else:
                                                    listaPrazos.append(np.nan)    
                                                listaOffsets.append(idx + 45)
                                                listaDatas.append('')
                                            else:
                                                idx = str(texto).find('fica estendido até o dia')
                                                if idx != -1:
                                                    listaPrazos.append(-1)
                                                    listaOffsets.append(idx + 25)
                                                    listaDatas.append(str(texto)[idx + 25:idx + 25 + 23])
                                                else:
                                                    idx = str(texto).find('até o dia')
                                                    if idx != -1:
                                                        listaPrazos.append(-1)
                                                        listaOffsets.append(idx + 10)
                                                        listaDatas.append(str(texto)[idx + 10:idx + 10 + 23])
                                                    else:
                                                        idx = str(texto).find('até às 18h do dia')
                                                        if idx != -1:
                                                            listaPrazos.append(-1)
                                                            listaOffsets.append(idx + 18)
                                                            listaDatas.append(str(texto)[idx + 18:idx + 18 + 23])
                                                        else:
                                                            idx = str(texto).find('estabelecido o período de')
                                                            if idx != -1:
                                                                listaPrazos.append(-2)
                                                                listaOffsets.append(idx + 26)
                                                                listaDatas.append(str(texto)[idx + 26:idx + 26 + 50])
                                                            else:
                                                                listaPrazos.append(np.nan)
                                                                listaOffsets.append(0)
                                                                listaDatas.append('')
    if (data_publicacao != '') and (len(listaPrazos) != 0) and (len(listaDatas) != 0):
        from datetime import datetime as dt
        from datetime import date
        if listaPrazos[0] == -1:
            dia, mes, ano, offset = data_tradutor(listaDatas[0])
        elif listaPrazos[0] == -2:
            texto = str(listaDatas[0])[:23].lstrip()
            dia, mes, ano, offset = data_tradutor(texto)
            texto = str(listaDatas[0])[offset + 7:]
            dia, mes, ano, offset = data_tradutor(texto)
        if dia != 0 and mes != 0 and ano != 0:
            data_final = dt.strptime(str(date(ano, mes, dia)), '%Y-%m-%d')
            data_inicial = dt.strptime(str(data_publicacao), '%Y-%m-%d %H:%M:%S')
            listaPrazos.pop(0)
            prazo  = abs((data_final - data_publicacao).days)
            listaPrazos.append(str(prazo))
    return listaPrazos