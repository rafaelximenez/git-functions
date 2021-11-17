# GIT Functions

[PT] Lib para funções do git.<br>
[EN] Lib for git functions.


## Funcionalidades:
* Checar se existem modificações

## Como usar:

### Instalação
```
    pip install gitfunctions
```

### Parâmetros

- remote_repository_name (Opcional): Nome do repositório remoto
- repo_path (Opcional): Caminho do projeto


### Exemplo
```
    from gitfunctions import gitfunctions

    git = gitfunctions.Git(repository_name='origin', repo_path='C:\\pasta_projeto')
    git.check_updates()
```

### Links:
[![Badge](https://img.shields.io/static/v1?label=Acesse&message=o%20site&color=yellowgreen)](https://github.com/strapbooll/git_functions)
