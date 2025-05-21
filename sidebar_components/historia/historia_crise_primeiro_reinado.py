import streamlit as st
import streamlit.components.v1 as components
#from streamlit_sortables import sort_items


def _crise_primeiro_reinado():
    # Tabs com conteúdos variados
    abas = st.tabs(["📖 Introdução", "🕒 Linha do Tempo",
                   "👤 Personagens", "Caça Palavras", "🧠 Quiz"])

    with abas[0]:
        st.header("Introdução")
        st.write("""
        A Crise do Primeiro Reinado (1822–1831) foi marcada por instabilidade política, econômica e social.
        A Confederação do Equador surge como uma reação ao autoritarismo de D. Pedro I.
        """)
        st.video("https://www.youtube.com/watch?v=_n6mLwFB1ss")
    with abas[1]:
        st.header("Linha do Tempo")
        st.markdown("""
        - **1822**: Independência do Brasil  
        - **1824**: Constituição outorgada  
        - **1824**: Eclosão da Confederação do Equador  
        - **1825**: Repressão e execução de líderes
        """)

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
                    "titulo": "Dom Pedro I",
                    "imagem": "data:image/jpeg;base64,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",
                    "nome": "Pedro de Alcântara Francisco António João Carlos Xavier de Paula Miguel Rafael Joaquim José Gonzaga Pascoal Cipriano Serafim",
                    "idade": "25 anos (em 1824)",
                    "carreira": "Imperador do Brasil",
                    "influencia": "Figura central do Império e da repressão à revolta",
                    "funcoes": "Autoridade máxima do Império, liderou a repressão"
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
        st.write("🎯 Encontre as palavras relacionadas à Crise do Primeiro Reinado!")
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
        const words = ["RECIFE", "OLINDA", "GOIANA", "ESCRAVOS", "JESUS"];
        let foundWords = [];
        let selectedCells = [];

        const grid = [
            ["S", "T", "O", "L", "I", "N", "D", "A", "T"],
            ["J", "E", "S", "U", "S", "N", "D", "A", "A"],
            ["J", "G", "O", "I", "A", "N", "A", "T", "P"],
            ["T", "S", "O", "V", "A", "R", "C", "S", "E"],
            ["B", "U", "G", "R", "E", "C", "I", "F", "E"]
        ];

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
        components.html(html_code, height=450)

    with abas[4]:
        st.header("Quiz Rápido: A Crise do Primeiro Reinado.")

        perguntas = [
    {
        "pergunta": "Quem foi uma das principais lideranças intelectuais da Confederação do Equador?",
        "alternativas": [
            "José Bonifácio",
            "Frei Caneca",
            "Dom Pedro I"
        ],
        "correta": "Frei Caneca"
    },
    {
        "pergunta": "Qual foi a principal motivação para o início da Confederação do Equador em 1824?",
        "alternativas": [
            "O descontentamento com a Constituição outorgada por Dom Pedro I",
            "A luta contra a escravidão",
            "A invasão das tropas portuguesas"
        ],
        "correta": "O descontentamento com a Constituição outorgada por Dom Pedro I"
    },
    {
        "pergunta": "Além de Pernambuco, qual outra província apoiou o movimento da Confederação do Equador?",
        "alternativas": [
            "Minas Gerais",
            "Ceará",
            "São Paulo"
        ],
        "correta": "Ceará"
    },
    {
        "pergunta": "O que aconteceu com Frei Caneca após o fracasso da Confederação do Equador?",
        "alternativas": [
            "Fugiu para Portugal",
            "Foi executado por fuzilamento",
            "Tornou-se conselheiro de Dom Pedro I"
        ],
        "correta": "Foi executado por fuzilamento"
    },
    {
        "pergunta": "Em qual cidade pernambucana se concentrou a maior resistência durante a Confederação do Equador?",
        "alternativas": [
            "Recife",
            "Olinda",
            "Goiana"
        ],
        "correta": "Goiana"
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
                resposta = st.session_state.get(f"resposta_deflagracao_revolta{i}")
                if resposta == p["correta"]:
                    acertos += 1
                else:
                    erros += 1

            st.markdown("---")
            st.success(f"✅ Total de acertos: **{acertos}**")
            st.error(f"❌ Total de erros: **{erros}**")
