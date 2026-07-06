name: Consolidar repositórios de estudos

# Roda manualmente: vá na aba "Actions" do repositório estudos-e-cursos,
# selecione este workflow na lista à esquerda, e clique em "Run workflow".
on:
  workflow_dispatch: {}

permissions:
  contents: write   # necessário para o job poder fazer commit/push de volta no repo

jobs:
  consolidar:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout do repositório estudos-e-cursos
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Consolidar repositórios de curso em subpastas
        env:
          GITHUB_USER: brunohss
        run: |
          set -euo pipefail

          declare -a REPOS=(
            "https://github.com/${GITHUB_USER}/DIO---Projeto-Eletronico.git|dio-projeto-eletronico|Curso DIO — Projeto Eletrônico"
            "https://github.com/${GITHUB_USER}/1Projeto-Docker-DIO.git|dio-docker-microsservicos|Curso DIO — Docker e Microsserviços (fork de toshiro-shibakita)"
            "https://github.com/${GITHUB_USER}/linux-projeto1-iac.git|dio-linux-projeto-1|Curso DIO — Linux, projeto 1 (IaC)"
            "https://github.com/${GITHUB_USER}/linux-projeto2-iac-.git|dio-linux-projeto-2|Curso DIO — Linux, projeto 2 (IaC)"
            "https://github.com/${GITHUB_USER}/dio-desafio-github.git|dio-desafio-github|Curso DIO — Desafio Git/GitHub"
            "https://github.com/${GITHUB_USER}/Python_Zumbis.git|python-zumbis|Curso Python para Zumbies — lista de exercícios"
            "https://github.com/${GITHUB_USER}/Python_Curso_em_Video.git|python-curso-em-video|Curso em Vídeo — exercícios de lógica em Python"
            "https://github.com/${GITHUB_USER}/FATEC---POO.git|fatec-poo|FATEC — Programação Orientada a Objetos (Java)"
            "https://github.com/${GITHUB_USER}/Estudo.git|estudo-geral|Material de estudo diverso"
          )

          INDICE_LINHAS=()

          for entrada in "${REPOS[@]}"; do
            IFS='|' read -r url pasta descricao <<< "$entrada"
            echo "----"
            echo "Repositório: $url"
            echo "Subpasta:    $pasta"

            TMP_DIR=$(mktemp -d)
            if git clone --depth 1 "$url" "$TMP_DIR"; then
              mkdir -p "$pasta"
              rsync -av --exclude='.git' "$TMP_DIR"/ "$pasta"/
              echo "OK: copiado para $pasta"
              INDICE_LINHAS+=("| [\`${pasta}\`](./${pasta}) | ${descricao} |")
            else
              echo "AVISO: falha ao clonar $url — pulando (verifique se o repositório é privado ou mudou de nome/URL)"
            fi
            rm -rf "$TMP_DIR"
          done

          {
            echo "# 📚 Estudos e Cursos"
            echo ""
            echo "> Repositório consolidado com exercícios e projetos de cursos realizados (DIO, Python, FATEC, etc)."
            echo "> Não faz parte do portfólio principal de projetos autorais — veja o"
            echo "> [portfólio principal](https://github.com/${GITHUB_USER}/${GITHUB_USER}) para os projetos técnicos completos."
            echo ""
            echo "## Conteúdo"
            echo ""
            echo "| Pasta | Descrição |"
            echo "|---|---|"
            printf '%s\n' "${INDICE_LINHAS[@]}"
            echo ""
            echo "---"
            echo "*Consolidado automaticamente a partir de repositórios individuais de curso (via GitHub Actions)."
          } > README.md

      - name: Commit e push das mudanças
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add .
          if git diff --cached --quiet; then
            echo "Nada novo para commitar."
          else
            git commit -m "Consolida repositórios de cursos e estudos em subpastas (automático)"
            git push
          fi
