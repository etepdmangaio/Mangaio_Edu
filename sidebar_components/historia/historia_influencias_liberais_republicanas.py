import streamlit as st
import streamlit.components.v1 as components
from streamlit_sortables import sort_items

def _historia_influe_liber_republ():
    abas = st.tabs(["📖 Introdução", "🕒 Linha do Tempo",
                   "👤 Personagens", "Caça Palavras", "🧠 Quiz"])
    
    with abas[0]:
            st.header("Introdução")
            texto = """A Confederação do Equador foi um movimento separatista influenciado por ideias liberais e republicanas, inspirado pela independência das colônias espanholas e pelos ideais da Revolução Francesa. Defendia a descentralização do poder, o federalismo e a liberdade de imprensa. Os líderes do movimento, como Frei Caneca, Cipriano Barata e Manuel de Carvalho, buscavam romper com o autoritarismo do Império. Esta Confederação surgiu como reação à imposição de Dom Pedro I sobre a Constituição outorgada. Apesar da repressão violenta, o movimento marcou a resistência liberal no Nordeste do Brasil."""
            # Usando HTML para justificar o texto
            html_texto = f"""
            <div style="text-align: justify; font-family: Arial, sans-serif; font-size: 16px;">
                {texto}
            </div>
            """
            # Exibindo o texto justificado no Streamlit
            st.markdown(html_texto, unsafe_allow_html=True)          
            st.video("https://www.youtube.com/watch?v=2vfKe0kBJw4")

    with abas[1]:
            st.header("Linha do Tempo")
            texto = ("""
            - **1789**: Revolução Francesa: difusão dos ideais de liberdade, igualdade e fraternidade.
                          
            - **1817**: Revolução Pernambucana: primeira grande tentativa de independência com ideais republicanos no Brasil.
                          
            - **1821**: Retorno de Dom João VI a Portugal e início do processo de centralização do poder por Dom Pedro I. 

            - **1824 (março)**: Outorga da Constituição de 1824 por Dom Pedro I, centralizadora e imposta sem participação popular.
                        
            - **1824 (julho)**: Eclosão da Confederação do Equador, influenciada pelas ideias liberais e pelo descontentamento com o autoritarismo imperial.
            """)
            html_texto = f"""
            <div style="text-align: justify; font-family: Arial, sans-serif; font-size: 16px;">
                {texto}
            </div>
            """
            st.markdown(html_texto, unsafe_allow_html=True)

    with abas[2]:
            st.header("Personagens Importantes")
            personagens = [
                {
                    "titulo": "Frei Caneca",
                    "imagem": "data:image/jpeg;base64,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",
                    "nome": "João Ribeiro Pessoa de Melo Montenegro",
                    "idade": "49 anos (em 1824)",
                    "carreira": "Religioso, jornalista e professor",
                    "influencia": "Um dos principais líderes intelectuais da Confederação do Equador",
                    "funcoes": "Articulador político, escritor de manifestos e líder ideológico"
                },
                {
                    "titulo": "Manoel de Carvalho Paes de Andrade",
                    "imagem": "data:image/jpeg;base64,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",
                    "nome": "Manoel de Carvalho Paes de Andrade",
                    "idade": "aproximadamente 36 anos (em 1824)",
                    "carreira": "Político e jornalista",
                    "influencia": "Presidente da província de Pernambuco e líder da proclamação da Confederação",
                    "funcoes": "Chefe político da revolta, proclamou a separação"
                },
                {
                    "titulo": "Cipriano Barata",
                    "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Domenico_Failutti_-_Retrato_de_Cipriano_Jos%C3%A9_Barata%2C_Acervo_do_Museu_Paulista_da_USP_%28cropped%29.jpg/250px-Domenico_Failutti_-_Retrato_de_Cipriano_Jos%C3%A9_Barata%2C_Acervo_do_Museu_Paulista_da_USP_%28cropped%29.jpg",
                    "nome": "Cipriano Barata de Almeida",
                    "idade": "Aproximadamente 58 anos (em 1824)",
                    "carreira": "Médico, político e jornalista",
                    "influencia": "Defensor do republicanismo e das ideias liberais, atuou na Confederação do Equador",
                    "funcoes": "Divulgador das ideias revolucionárias, articulador político e crítico do governo imperial"
                },
            ]

            for p in personagens:
                st.subheader(p["titulo"])
                col1, col2 = st.columns([1, 3])

                with col1:
                    st.image(p["imagem"], width=150)

                with col2:
                    st.markdown(f"""
                    **Nome completo:** {p["nome"]}  
                    **Idade em 1824:** {p["idade"]}  
                    **Carreira:** {p["carreira"]}  
                    **Influência:** {p["influencia"]}  
                    **Funções:** {p["funcoes"]}
                    """)
                st.markdown("---")

    with abas[3]:

        st.header("Caça-palavras")
        st.write("🎯 Encontre as palavras relacionadas as influências liberais e republicanas!")
        html_code = """
        <style>
        table {
            border-collapse: collapse;
            margin-bottom: 10px;
            background-color: white;
        }
        td {
            border: 3px solid rgb(41, 222, 216);
            padding: 10px;
            text-align: center;
            font-weight: bold;
            cursor: pointer;
            user-select: none;
        }
        td.selected {
            background-color: yellow;
        }
        td.found {
            background-color: lightgreen;
        }    
        p, span, h5, mark, b {
            color: #4CAF50;
            background-color: transparent !important;
        }
        mark {
            background-color: transparent !important;
        }
        button {
            padding: 10px 20px;
            border-radius: 10px;
            background-color: #4CAF50; /* verde suave */
            color: white;
            border: none;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        button:active {
            background-color: #3e8e41;
            transform: scale(0.98);
        }    
        </style>

        <div id="game"></div>
        <button onclick="checkWord()">Verificar</button>
        <p id="status"></p>
        <p><b>Palavras para encontrar:</b> <span id="word-list"></span></p>

        <script>
        const words = ["MOVIMENTO", "LIBERAIS", "SEPARATISTA", "AUTORITARISMO", "DESCENTRALIZADO", "REVOLUCAO", "REPRESSAO", "NORDESTE", "VIOLENCIA", "COLONIAS", "OUTORGADA", "IMPOSICAO", "CONSTITUICAO, INFLUENCIAS", "REPUBLICANAS"];
        let foundWords = [];
        let selectedCells = [];

        const grid = [
            ["M", "T", "L", "I", "B", "E", "R", "I", "S", "E", "O", "A", "I", "R", "E", "A", "M", "U"],
            ["O", "A", "T", "E", "R", "G", "A", "D", "A", "A", "A", "L", "A", "E", "E", "O", "U", "A"],
            ["V", "A", "U", "V", "O", "O", "L", "E", "N", "C", "C", "A", "S", "P", "A", "U", "A", "I"],
            ["I", "N", "F", "T", "U", "T", "O", "R", "G", "O", "I", "A", "L", "R", "O", "T", "N", "C"],
            ["M", "U", "O", "C", "O", "O", "N", "I", "U", "A", "S", "L", "I", "E", "S", "O", "E", "C"],
            ["E", "E", "R", "E", "O", "R", "M", "R", "L", "A", "O", "D", "I", "S", "A", "R", "L", "O"],
            ["N", "T", "E", "C", "R", "N", "I", "I", "F", "A", "P", "T", "E", "S", "T", "G", "A", "L"],
            ["T", "S", "V", "A", "G", "A", "S", "R", "N", "A", "M", "L", "P", "A", "I", "D", "N", "O"],
            ["O", "E", "O", "O", "A", "S", "S", "T", "A", "R", "I", "A", "T", "O", "T", "A", "I", "N"],
            ["A", "D", "L", "P", "D", "S", "S", "K", "I", "R", "T", "A", "U", "I", "S", "O", "I", "I"],
            ["C", "R", "U", "P", "E", "P", "A", "R", "A", "T", "I", "S", "T", "A", "S", "V", "I", "A"],
            ["F", "O", "C", "P", "L", "R", "M", "O", "I", "N", "U", "S", "U", "E", "C", "E", "A", "S"],
            ["A", "N", "A", "V", "I", "O", "L", "E", "N", "C", "I", "I", "M", "S", "O", "R", "M", "I"],
            ["C", "R", "O", "P", "A", "E", "S", "S", "E", "S", "T", "A", "C", "O", "S", "T", "I", "A"],
            ["F", "O", "I", "V", "I", "O", "L", "E", "N", "C", "P", "A", "N", "A", "C", "S", "E", "D"],
            ["H", "I", "H", "O", "D", "A", "Z", "I", "L", "A", "R", "T", "N", "E", "O", "S", "A", "O"],
            ["F", "W", "I", "O", "D", "A", "Z", "I", "L", "A", "R", "T", "N", "E", "C", "S", "E", "D"],
            ["B", "S", "E", "P", "A", "R", "A", "T", "I", "S", "T", "A", "T", "A", "O", "T", "I", "S"]
        ]            
        
        function renderGrid() {
            let html = "<table>";
            for (let i = 0; i < grid.length; i++) {
            html += "<tr>";
            for (let j = 0; j < grid[i].length; j++) {
                html += `<td onclick="selectCell(this, ${i}, ${j})" data-i="${i}" data-j="${j}">${grid[i][j]}</td>`;
            }
            html += "</tr>";
            }
            html += "</table>";
            document.getElementById("game").innerHTML = html;
            document.getElementById("word-list").textContent = words.join(", ");
        }

        function selectCell(cell, i, j) {
            if (cell.classList.contains("found")) return;

            if (cell.classList.contains("selected")) {
            cell.classList.remove("selected");
            selectedCells = selectedCells.filter(c => !(c.i === i && c.j === j));
            } else {
            cell.classList.add("selected");
            selectedCells.push({ i, j, letter: grid[i][j], cell });
            }
        }

        function checkWord() {
            if (selectedCells.length < 2) {
                document.getElementById("status").textContent = "❌ Selecione pelo menos duas letras em sequência.";
                clearSelection();
                return;
            }

            // Verifica direção entre os dois primeiros pontos
            const dx = selectedCells[1].i - selectedCells[0].i;
            const dy = selectedCells[1].j - selectedCells[0].j;

            // Valida se todos os próximos seguem essa mesma direção
            for (let k = 2; k < selectedCells.length; k++) {
                const currentDx = selectedCells[k].i - selectedCells[k - 1].i;
                const currentDy = selectedCells[k].j - selectedCells[k - 1].j;
                if (currentDx !== dx || currentDy !== dy) {
                    document.getElementById("status").textContent = "❌ As letras precisam estar em sequência reta.";
                    clearSelection();
                    return;
                }
            }

            const formedWord = selectedCells.map(c => c.letter).join("").toUpperCase();

            if (words.includes(formedWord) && !foundWords.includes(formedWord)) {
                selectedCells.forEach(c => c.cell.classList.add("found"));
                foundWords.push(formedWord);
                document.getElementById("status").textContent = `✅ Palavra encontrada: ${formedWord}`;
            } else {
                document.getElementById("status").textContent = `❌ Palavra inválida: ${formedWord}`;
            }

            clearSelection();
        }

        function clearSelection() {
            selectedCells.forEach(c => c.cell.classList.remove("selected"));
            selectedCells = [];
        }

        renderGrid();
        </script>
        """
        components.html(html_code, height=1000)        
    
    with abas[4]:
            st.markdown("## Quiz Rápido: Influências Liberais e Republicanas")
            st.write("Responda as perguntas abaixo para testar seus conhecimentos sobre a Confederação do Equador e suas influências liberais e republicanas.")

            perguntas = [
                {
                    "pergunta": "Qual o significado da palavra entre a seguir: outorgada?",
                    "alternativas": [
                        "Incapacitada",
                        "Aprovada",
                        "Inocentada",                        
                        "Misteriosa",
                        "Indeferida"
                    ],
                    "correta": "Aprovada"
                },               
                {
                    "pergunta": "Quais as característica da Constituição de 1824 outorgada por D. Pedro I?",
                    "alternativas": [
                        "Liberal e republicana",
                        "Descentralizadora e democrática",
                        "Centralizadora e autoritária",
                        "Republicana e descentralizadora",
                        "Autoritária e democrática"
                    ],
                    "correta": "Centralizadora e autoritária"
                },             
                {
                    "pergunta": "Quais os poderes possuia D. Pedro I segundo a Constituição de 1824?",
                    "alternativas": [
                        "Poder Executivo e Legislativo",
                        "Poder Executivo e Judiciário",
                        "Poder Legislativo e Judiciário",
                        "Poder Executivo, Legislativo e Judiciário",
                        "Poder Executivo e Moderador"
                    ],
                    "correta": "Poder Executivo e Moderador"
                },
                {
                    "pergunta": "Qual a nação que emprestou dinheiro ao imperador D. Pedro I para que fosse possível comprar armas, navios e contratar mercenários para por um fim à Confederação do Equador liderada por Pernambuco?",
                    "alternativas": [
                        "Inglaterra",
                        "França",
                        "Alemanha",
                        "China",
                        "Estados Unidos da América"
                    ],
                    "correta": "Inglaterra"
                },
                {
                    "pergunta": "Quais as duas principais influências que motivaram a Confederação do Equador e o que provocou o estopim (gatilho) da mesma?",
                    "alternativas": [
                        "O absolutismo, o iluminismo e a Revolução Francesa.",
                        "A Revolução Industrial, a Revolução Francesa e a independência dos Estados Unidos.",
                        "A pobreza do população, a desigualdade política e os altos impostos.",
                        "Algumas independências da América, os gloriosos dias da Revolução Francesa e a Constituição de 1824 imposta pelo imperador D. Pedro I.",
                        "o iluminismo, a Revolução Francesa e a independência do Brasil."                 
                    ],
                    "correta": "Algumas independências da América, os gloriosos dias da Revolução Francesa e a Constituição de 1824 imposta pelo imperador D. Pedro I."
                }
            ]

            acertos = 0
            erros = 0

            for i, p in enumerate(perguntas):
                st.subheader(f"{i+1}. {p['pergunta']}")
                resposta = st.radio(
                    "Escolha uma alternativa:",
                    options=p["alternativas"],
                    key=f"resposta_deflagracao_revolta{i}"
                )

            # Verificação e contagem (fora do loop de exibição das perguntas)
            if st.button("Ver resultado"):
                for i, p in enumerate(perguntas):
                    resposta = st.session_state.get(
                        f"resposta_deflagracao_revolta{i}")
                    if resposta == p["correta"]:
                        acertos += 1
                    else:
                        erros += 1

                st.markdown("---")
                st.success(f"✅ Total de acertos: **{acertos}**")
                st.error(f"❌ Total de erros: **{erros}**")

            # for i, p in enumerate(perguntas):
            #     st.markdown(f"### {i+1}. {p['pergunta']}")
            #     col1, col2, col3, col4, col5 = st.columns(5)

            #     # Usando chaves únicas no st.session_state para isolar as respostas
            #     if f"resposta_consequencias_{i}" not in st.session_state:
            #         st.session_state[f"resposta_consequencias_{i}"] = None

            #     for j, alternativa in enumerate(p["alternativas"]):
            #         col = [col1, col2, col3, col4, col5][j % 5]
            #         if col.button(f"{alternativa}", key=f"q1_{i}_a{j}"):
            #             st.session_state[f"resposta_consequencias_{i}"] = alternativa

            #     resposta = st.session_state[f"resposta_consequencias_{i}"]
            #     if resposta:
            #         if resposta == p["correta"]:
            #             st.success(f"✅ Boa! Resposta correta: **{resposta}**")
            #         else:
            #             st.error(f"❌ Opa! Resposta errada: **{resposta}**\n\n💡 Resposta certa: **{p['correta']}**")
