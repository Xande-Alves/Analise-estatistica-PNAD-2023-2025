import os
import pandas as pd
import requests
import zipfile
import io

arquivo_saida = "pnad_2023_2025_resumo.csv"

if os.path.exists(arquivo_saida):
    os.remove(arquivo_saida)

primeiro = True

# ============================================
# CARREGA TABELA CNAE
# ============================================

cnae_df = pd.read_excel(
    "Estrutura_Atividade_CNAE_Domiciliar_2_0.xls",
    header=2
)

# Mantém somente colunas necessárias
cnae_df = cnae_df.iloc[:, :4]

cnae_df.columns = [
    "secao",
    "divisao",
    "classe",
    "descricao"
]

# Converte strings vazias em NaN
cnae_df = cnae_df.replace(r'^\s*$', pd.NA, regex=True)

# Preenche seção e divisão para baixo
cnae_df["secao"] = cnae_df["secao"].ffill()
cnae_df["divisao"] = cnae_df["divisao"].ffill()

# Mantém apenas linhas que possuem classe CNAE
cnae_classes = cnae_df[cnae_df["classe"].notna()].copy()

# Padroniza classe
cnae_classes["classe"] = (
    cnae_classes["classe"]
    .astype(str)
    .str.extract(r"(\d+)")[0]
    .str.zfill(5)
)

# Padroniza divisão
cnae_classes["divisao"] = (
    cnae_classes["divisao"]
    .astype(str)
    .str.extract(r"(\d+)")[0]
    .str.zfill(2)
)

# Padroniza seção
cnae_classes["secao"] = (
    cnae_classes["secao"]
    .astype(str)
    .str.strip()
)

# Cria dicionários
map_secao = dict(zip(cnae_classes["classe"], cnae_classes["secao"]))
map_divisao = dict(zip(cnae_classes["classe"], cnae_classes["divisao"]))

for ano in range(2023, 2026):
    for tri in [1, 2, 3, 4]:

        if ano == 2025:
            url = f"https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Trimestral/Microdados/{ano}/PNADC_{tri:02d}{ano}.zip"
        else:
            if ano == 2024 and tri == 2:
                url = f"https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Trimestral/Microdados/{ano}/PNADC_{tri:02d}{ano}_20260324.zip"
            else:
                url = f"https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Trimestral/Microdados/{ano}/PNADC_{tri:02d}{ano}_20250815.zip"

        print(f"Baixando {ano} T{tri}...")

        try:
            r = requests.get(url)
            r.raise_for_status()
        except:
            r = requests.get(url, verify=False)
            r.raise_for_status()
            continue

        z = zipfile.ZipFile(io.BytesIO(r.content))

        for file in z.namelist():
            if file.endswith(".txt"):
                with z.open(file) as f:

                    for chunk in pd.read_fwf(
                        f,
                        colspecs=[
                            (0, 4),    # Ano
                            (4, 5),    # Trimestre
                            (5, 7),    # UF
                            (7, 9),    # Capital
                            (9, 11),   # RM_RIDE
                            (11, 20),  # UPA
                            (20, 27),  # Estrato
                            (27, 29),  # V1008
                            (29, 31),  # V1014
                            (31, 32),  # V1016
                            (32, 33),  # V1022
                            (33, 34),  # V1023
                            (34, 49),  # V1027
                            (49, 64),  # V1028
                            (64, 73),  # V1029
                            (73, 82),  # V1033
                            (82, 85),  # posest
                            (85, 88),  # posest_sxi
                            (88, 90),  # V2001
                            (94, 95),  # V2007
                            (103, 106),  # V2009
                            (106, 107),  # V2010
                            (124, 126),  # V3009A
                            (134, 135),  # V3014
                            (136, 137),  # V4002
                            (155, 156),  # V4012
                            (157, 162),  # V4013
                            (163, 164),  # V40132A
                            (165, 166),  # V4015
                            (166, 167),  # V40151
                            (167, 168),  # V401511
                            (168, 170),  # V401512
                            (170, 171),  # V4016
                            (171, 172),  # V40161
                            (172, 174),  # V40162
                            (174, 176),  # V40163
                            (176, 177),  # V4017
                            (177, 178),  # V40171
                            (178, 179),  # V401711
                            (179, 180),  # V4018
                            (180, 181),  # V40181
                            (181, 183),  # V40182
                            (183, 185),  # V40183
                            (185, 186),  # V4019
                            (186, 187),  # V4020
                            (187, 188),  # V4021
                            (188, 189),  # V4022
                            (189, 190),  # V4024
                            (190, 191),  # V4025
                            (191, 192),  # V4026
                            (192, 193),  # V4027
                            (193, 194),  # V4028
                            (194, 195),  # V4029
                            (195, 196),  # V4032
                            (196, 197),  # V4033
                            (197, 198),  # V40331
                            (199, 207),  # V403312
                            (209, 217),  # V403322
                            (219, 220),  # V4034
                            (222, 230),  # V403412
                            (232, 240),  # V403422
                            (240, 243),  # V4039
                            (243, 246),  # V4039C
                            (257, 258),  # V4043
                            (259, 264),  # V4044
                            (264, 265),  # V4045
                            (265, 266),  # V4046
                            (267, 268),  # V4048
                            (269, 270),  # V4050
                            (270, 271),  # V40501
                            (272, 280),  # V405012
                            (292, 293),  # V4051
                            (293, 294),  # V40511
                            (295, 303),  # V405112
                            (305, 313),  # V405122
                            (347, 355),  # V405912
                            (357, 365)  # V405922
                        ],
                        names=[
                            "ANO", "TRIMESTRE", "UF", "Capital", "RM_RIDE", "UPA", "Estrato",
                            "V1008", "V1014", "V1016", "V1022", "V1023", "V1027", "V1028",
                            "V1029", "V1033", "posest", "posest_sxi", "V2001", "V2007",
                            "V2009", "V2010", "V3009A", "V3014", "V4002", "V4012", "V4013",
                            "V40132A", "V4015", "V40151", "V401511", "V401512", "V4016",
                            "V40161", "V40162", "V40163", "V4017", "V40171", "V401711",
                            "V4018", "V40181", "V40182", "V40183", "V4019", "V4020",
                            "V4021", "V4022", "V4024", "V4025", "V4026", "V4027",
                            "V4028", "V4029", "V4032", "V4033", "V40331", "V403312",
                            "V403322", "V4034", "V403412", "V403422", "V4039", "V4039C",
                            "V4043", "V4044", "V4045", "V4046", "V4048", "V4050",
                            "V40501", "V405012", "V4051", "V40511", "V405112",
                            "V405122", "V405912", "V405922"
                        ],
                        dtype={
                            "ANO": "Int16",
                            "TRIMESTRE": "Int8",
                            "UF": "Int8",
                            "V2001": "Int8"
                        },
                        chunksize=100000
                    ):
                        chunk = chunk[chunk["UF"] == 26]

                        # Padroniza V4013
                        chunk["V4013"] = (
                            chunk["V4013"]
                            .astype(str)
                            .str.replace(".0", "", regex=False)
                            .str.zfill(5)
                        )

                        # Cria novas colunas
                        chunk["secao_cnae"] = chunk["V4013"].map(map_secao)
                        chunk["divisao_cnae"] = chunk["V4013"].map(map_divisao)

                        chunk.to_csv(
                            arquivo_saida,
                            mode="a",
                            header=primeiro,
                            index=False
                        )

                        primeiro = False

print("Arquivo final gerado!")
