#!/usr/bin/env bash
#
# consolidar-estudos.sh
#
# Consolida os repositórios de cursos/estudos do GitHub (brunohss) em um único
# repositório "estudos-e-cursos", cada um em sua própria subpasta.
#
# PRÉ-REQUISITOS:
#   1. Ter criado manualmente no GitHub um repositório vazio chamado "estudos-e-cursos"
#      (com um README inicial, ou totalmente vazio — o script cuida disso).
#   2. Ter git, rsync e acesso configurado (SSH ou HTTPS com credenciais salvas).
#
# COMO USAR:
#   chmod +x consolidar-estudos.sh
#   ./consolidar-estudos.sh
#
# O que o script faz:
#   - Clona o repositório "estudos-e-cursos" (ou usa a pasta local, se já existir)
#   - Para cada repositório de curso, clona numa pasta temporária, copia o
#     conteúdo (sem a pasta .git) para a subpasta correspondente
#   - Gera automaticamente um README.md de índice na raiz
#   - Faz commit e push de tudo
#
# O que o script NÃO faz (por segurança):
#   - Não apaga nem arquiva os repositórios originais — isso você faz manualmente
#     depois de conferir que a cópia deu certo (Settings > Danger Zone > Archive)

set -euo pipefail

GITHUB_USER="brunohss"
REPO_DESTINO="estudos-e-cursos"
URL_DESTINO="https://github.com/${GITHUB_USER}/${REPO_DESTINO}.git"

# Lista de repositórios a consolidar: "url|subpasta|descrição curta"
REPOS=(
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

echo "==> Clonando (ou atualizando) o repositório de destino: ${REPO_DESTINO}"
if [ -d "${REPO_DESTINO}/.git" ]; then
  cd "${REPO_DESTINO}"
  git pull
else
  git clone "${URL_DESTINO}" "${REPO_DESTINO}"
  cd "${REPO_DESTINO}"
fi

echo "==> Consolidando repositórios em subpastas..."
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
    echo "AVISO: falha ao clonar $url — pulando (verifique se o nome/URL mudou)"
  fi
  rm -rf "$TMP_DIR"
done

echo "==> Gerando README.md de índice..."
cat > README.md << EOF
# 📚 Estudos e Cursos

> Repositório consolidado com exercícios e projetos de cursos realizados (DIO, Python, FATEC, etc).
> Não faz parte do portfólio principal de projetos autorais — veja o
> [portfólio principal](https://github.com/${GITHUB_USER}/${GITHUB_USER}) para os projetos técnicos completos.

## Conteúdo

| Pasta | Descrição |
|---|---|
$(printf '%s\n' "${INDICE_LINHAS[@]}")

---
*Consolidado automaticamente a partir de repositórios individuais de curso.*
EOF

echo "==> Commit e push"
git add .
git commit -m "Consolida repositórios de cursos e estudos em subpastas" || echo "Nada novo para commitar"
git push

echo "==> Concluído!"
echo "Confira o resultado em: https://github.com/${GITHUB_USER}/${REPO_DESTINO}"
echo ""
echo "PRÓXIMO PASSO (manual): depois de conferir que está tudo certo,"
echo "arquive os repositórios originais em Settings > Danger Zone > Archive this repository."
