# Link para download do git
- [Baixa git](https://git-scm.com/downloads)

# Configurando  ferramenta

## Configurações de usuários

#### Configura o nome que você quer ligado as suas transações de commit
```
git config --global user.name "[nome]"
```

Configurando email
```
git config --global user.email "[seu email]]"
```


## Criando Repositórios

Criado um novo repositório local
```
git init [nome do projeto]
```

Clonando repositórios
```
git clone [url]
```

## Fazendo Mudanças
Revisando edições e criando transações de commit

Listando todos os arquivos novos ou modificados para serem commitados
```
git status
```

Mostrando a diferença nos arquivos que não foram realizados
```
git diff
```

Mostrando a diferença entre arquivos selecionados e suas últimas versões
```
git diff --staged
```

Faz o snapshot de um arquivo na preparação para versionamento
```
git add [arquivo]
```

Deseleciona o arquivo, mas preserva seu conteúdo
```
git reset [arquivo]
```

Grava o snapshot premanentemenete do arquivo no histórico de versão
```
git commit -m "[mensagem descritiva]"
```

## Mudanças em grupo
Nomeie uma série de commits e combine os esforços completos

Lista todos os branches locais no repositório atual

```
git branch
```
Criando uma nova branch

```
git branch [nome-do-branch]
```

Mudando para o branch específico e atualiza o diretório de trabalho

```
git checkout [nome-do-branch]
```

Combina o histórico do branch específico com o branch atual
```
git merge [branch]
```
W
Exclui o branch específico
```
git branch -d [nome-do-branch]
```

## Refatorando nomes de arquivos

Mude e remova os arquivos versionados
Remove o arquivo do diretório de trabalho e o seleciona para remoção
```
git rm --cached [arquivo]
```
Remove o arquivo do controle de versão mas preserva o arquivo
localmente
```
git rm [arquivo]
```
Muda o nome do arquivo e o seleciona para o commit
```
git mv [arquivo-original] [arquivo-renomeado]
```

## Suprimindo o rastreamento
Exclua arquivos e diretórios temporários

Um arquivo de texto chamado `.gitignore` suprime o versionamento
acidental de arquivos e diretórios correspondentes aos padrões
específicados

```
*.log
build/
temp-*
```

Lista todos os arquivos ignorados neste projeto
```
git ls-files --other --ignored --exclude-standard
```

## Salvando fragmentos
Arquive e restaure mudanças incompletas
Armazena temporariamente todos os arquivos rastreados modificados

```
 git stash
```
Lista todos os conjuntos de alterações em stash
```
git stash list
```
Restaura os arquivos recentes em stash
```
git stash pop
```
Descarta os conjuntos de alterações mais recentes em stash
```
git stash drop
```

## Revisando o histórico

Navegue e inspecione a evolução dos arquivos do projeto
Lista o histórico de versões para o branch atual
```git log
```
Lista o histórico de versões para um arquivo, incluindo mudanças de
nome
```
git log --follow [arquivo]
```
Mostra a diferença de conteúdo entre dois branches
```
git diff [primerio-branch]...[segundo-branch]
```
Retorna mudanças de metadata e conteúdo para o commit especificado
```
git show [commit]
```

## Desfazendo commits

Apague enganos e crie um histórico substituto

Desfaz todos os commits depois de `[commit]`, preservando
mudanças locais
```
git reset [commit]
```

Descarta todo histórico e mudanças para o commit especificado
```
git reset --hard [commit]
```

## Sincronizando as mudanças
Registre um marcador de repositório e troque o histórico de versão

Baixe todo o histórico de um marcador de repositório
```
git fetch [marcador]
```
Combina o marcador do branch no branch local
```
git merge [marcador]/[branch]
```
Envia todos os commits do branch local para o GitHub
```
git push [alias] [branch]
```
Baixa o histórico e incorpora as mudanças
```
git pull
```