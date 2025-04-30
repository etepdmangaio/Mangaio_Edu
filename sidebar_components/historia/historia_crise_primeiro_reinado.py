import streamlit as st
import streamlit.components.v1 as components
from streamlit_sortables import sort_items


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
        st.write("""
        - **Frei Caneca** – líder intelectual e político.
        - **Dom Pedro I** – Imperador autoritário que centralizou o poder.
        """)

    with abas[3]:

        st.header("Caça-palavras")
        st.write("🎯 Encontre as palavras relacionadas à Crise do Primeiro Reinado!")
        st.write("RECIFE", ", OLINDA", ", GOIANA", ", ESCRAVOS", ", JESUS")
        html_code = """
        <style>
        table {
            border-collapse: collapse;
            margin-bottom: 10px;
        }
        td {
            border: 1px solid white;
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
        p{
            color: white;
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
