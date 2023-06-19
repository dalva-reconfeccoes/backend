from urllib.parse import urlencode
from urllib.request import urlopen
from bs4 import BeautifulSoup
from xml.dom import minidom
from pytz import unicode
import re


class Correios(object):
    PAC = 41106
    SEDEX = 40010
    SEDEX_10 = 40215
    SEDEX_HOJE = 40290
    E_SEDEX = 81019
    OTE = 44105
    NORMAL = 41017
    SEDEX_A_COBRAR = 40045

    def __init__(self):
        self.base_url_calc_term = (
            "http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx"
        )
        self.base_url_verify_cep = (
            "http://cep.republicavirtual.com.br/web_cep.php?formato="
        )
        self.base_url_verify_order = (
            "http://websro.correios.com.br/sro_bin/txect01$.QueryList?"
        )

    def _getDados(self, tags_name, dom):
        data = {}
        for tag_name in tags_name:
            try:
                data[tag_name] = dom.getElementsByTagName(tag_name)[0]
                data[tag_name] = data[tag_name].childNodes[0].data
            except (IndexError, KeyError):
                data[tag_name] = ""

        return data

    def frete(self, **kwargs):
        if "mao_propria" not in kwargs.keys():
            kwargs["mao_propria"] = "N"
        if "valor_declarado" not in kwargs.keys():
            kwargs["valor_declarado"] = "0"
        if "aviso_recebimento" not in kwargs.keys():
            kwargs["aviso_recebimento"] = "N"
        if "empresa" not in kwargs.keys():
            kwargs["empresa"] = ""
        if "senha" not in kwargs.keys():
            kwargs["senha"] = ""
        if "toback" not in kwargs.keys():
            kwargs["toback"] = "xml"

        fields = [
            ("nCdEmpresa", kwargs["empresa"]),
            ("sDsSenha", kwargs["senha"]),
            ("nCdServico", kwargs["cod"]),
            ("sCepOrigem", kwargs["HERECEP"]),
            ("sCepDestino", kwargs["GOCEP"]),
            ("nVlPeso", kwargs["peso"]),
            ("nCdFormato", kwargs["formato"]),
            ("nVlComprimento", kwargs["comprimento"]),
            ("nVlAltura", kwargs["altura"]),
            ("nVlLargura", kwargs["largura"]),
            ("nVlDiametro", kwargs["diametro"]),
            ("sCdMaoPropria", kwargs["mao_propria"]),
            ("nVlValorDeclarado", kwargs["valor_declarado"]),
            ("sCdAvisoRecebimento", kwargs["aviso_recebimento"]),
            ("StrRetorno", kwargs["toback"]),
        ]

        url = self.base_url_calc_term + "?" + urlencode(fields)
        dom = minidom.parse(urlopen(url))

        tags_name = (
            "MsgErro",
            "Erro",
            "Codigo",
            "Valor",
            "PrazoEntrega",
            "ValorMaoPropria",
            "ValorValorDeclarado",
            "EntregaDomiciliar",
            "EntregaSabado",
        )

        return self._getDados(tags_name, dom)

    def cep(self, numero):
        url = f"{self.base_url_verify_cep}xml&cep={numero}"
        dom = minidom.parse(urlopen(url))

        tags_name = (
            "uf",
            "cidade",
            "bairro",
            "tipo_logradouro",
            "logradouro",
        )

        elements = dom.getElementsByTagName("resultado")[0]
        element = int(elements.childNodes[0].data)
        if element != 0:
            return self._getDados(tags_name, dom)
        else:
            return {}

    def encomenda(self, numero):
        url = f"{self.base_url_verify_order}P_ITEMCODE=&P_LINGUA=001&P_TESTE=&P_TIPO=001&P_COD_UNI={numero}"
        html = urlopen(url).read()
        table = re.search(r"<table.*</TABLE>", html, re.S).group(0)
        parsed = BeautifulSoup(table)
        dados = []
        for count, tr in enumerate(parsed.table):
            if count > 4 and str(tr).strip() != "":
                if re.match(r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}", tr.contents[0].string):
                    dados.append(
                        {
                            "data": unicode(tr.contents[0].string),
                            "local": unicode(tr.contents[1].string),
                            "status": unicode(tr.contents[2].font.string),
                        }
                    )

                else:
                    dados[len(dados) - 1]["detalhes"] = unicode(tr.contents[0].string)

        return dados
