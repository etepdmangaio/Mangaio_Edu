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
            texto = ("""
            - **Frei Caneca (Joaquim do Amor Divino Caneca)** – Religioso, jornalista e intelectual, foi um dos principais ideólogos do movimento. Defensor do republicanismo, federalismo e da liberdade de expressão. Era carismático e articulador político.
                     
            - **Cipriano Barata** – Médico, jornalista e ativista político, conhecido por sua linguagem inflamada e defesa intransigente da liberdade. Atuou em várias revoltas e propagava ideias iluministas e republicanas.
                     
            - **Manuel de Carvalho Paes de Andrade** – Presidente da província de Pernambuco e líder civil da Confederação. Apoiou a causa republicana e foi peça central na proclamação do governo confederado.
                     
            - **Pedro Ivo Veloso da Silveira** – Militar e líder da resistência armada. Comandou as forças confederadas no interior, sendo símbolo da luta até os últimos momentos do movimento.
            """)

            html_texto = f"""
            <div style="text-align: justify; font-family: Arial, sans-serif; font-size: 16px;">
                {texto}
            </div>
            """
            st.markdown(html_texto, unsafe_allow_html=True)

    with abas[3]:

        st.header("Caça-palavras")
        st.write("🎮 Aqui é onde o jogo vai!")
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
        button {
            padding: 10px 20px;
            border-radius: 10px;
            background-color: #4CAF50; 
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
        h5{
            color: #EDEDED;
        }
        mark{
            color: #EDEDED;
            background-color: transparent !important;
        }     
        </style>

        <div id="game"></div>
        <button onclick="checkWord()">Verificar</button>
        <p id="status"></p>
        <p><b><mark>Palavras para encontrar:</mark></b> <h5><span id="word-list"></span><h5></p>

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
            const formedWord = selectedCells.map(c => c.letter).join("");
            const upperWord = formedWord.toUpperCase();
            const status = document.getElementById("status");

            if (words.includes(upperWord) && !foundWords.includes(upperWord)) {
            selectedCells.forEach(c => c.cell.classList.add("found"));
            foundWords.push(upperWord);            

            status.textContent = `✅ Palavra encontrada: ${upperWord}`;
            } else {
            status.textContent = `❌ Palavra inválida: ${upperWord}`;
            }

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
