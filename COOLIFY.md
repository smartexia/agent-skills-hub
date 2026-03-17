# Coolify

Este projeto agora pode ser publicado no Coolify como uma aplicação com `Dockerfile`.

## Como funciona

- O build executa `python build_page.py`
- O resultado gerado (`index.html`) é servido por `nginx`
- O endpoint de health check está em `/healthz`

## Configuração sugerida no Coolify

- Build pack: `Dockerfile`
- Port: `80`
- Health check path: `/healthz`

## Deploy

1. Suba este repositório para o Git remoto que você conecta no Coolify.
2. Crie um novo projeto no Coolify apontando para esse repositório.
3. Selecione o `Dockerfile` da raiz.
4. Configure a porta `80`.
5. Opcionalmente, use um domínio customizado e HTTPS pelo próprio Coolify.

## Atualizando a página

Sempre que você alterar agentes ou skills, rode:

```bash
python build_page.py
```

Isso atualiza o `index.html` localmente e o mesmo processo também roda durante o build do container.
