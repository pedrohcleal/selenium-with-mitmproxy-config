![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/selenium-43B02A?style=flat&logo=selenium&logoColor=white)
![MITM Proxy](https://img.shields.io/badge/mitmproxy-FF5733?style=flat&logo=mitmproxy&logoColor=white)
![JSON](https://img.shields.io/badge/json-000000?style=flat&logo=json&logoColor=white)
![WebDriver Manager](https://img.shields.io/badge/webdriver--manager-0000FF?style=flat&logo=googlechrome&logoColor=white)

# Selenium com MITM Proxy

Este projeto demonstra como integrar o [Selenium](https://www.selenium.dev/) com o [MITM Proxy](https://mitmproxy.org/) para interceptar e salvar respostas HTTP. A aplicação busca dados de produtos do site Kabum e os registra em arquivos JSON para análise posterior.

## Estrutura do Projeto

```
.
├── src
│   ├── main.py            # Ponto de entrada da aplicação
│   ├── chrome_config.py   # Configuração do driver Chrome do Selenium com proxy
│   ├── mitm_script.py     # Script do MITM Proxy para interceptação de respostas HTTP
├── products               # Diretório onde os arquivos JSON são salvos
```

## Pré-requisitos

- Python 3.9+
- Google Chrome instalado
- [MITM Proxy](https://mitmproxy.org/) instalado
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager) para gerenciar o ChromeDriver

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/pedrohcleal/selenium-with-proxy-config.git
   cd selenium-with-proxy-config
   ```

1. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Inicie a aplicação:

   ```bash
   python src/main.py
   ```

   Isso irá:

   - Iniciar o MITM Proxy na porta 8090.
   - Abrir o site da Kabum usando um navegador Chrome sem interface gráfica (headless).
   - Salvar os dados interceptados das respostas HTTP como arquivos JSON no diretório `products`.

1. Visualize os arquivos JSON gerados:

   - Navegue até o diretório `products` para encontrar os dados interceptados.

## Visão Geral do Código

### `src/main.py`

Este script inicializa o driver Selenium, navega até o site da Kabum e processa o arquivo JSON mais recente.

### `src/chrome_config.py`

Configura o driver Chrome do Selenium com as configurações do MITM Proxy. Principais características:

- Modo headless (sem interface gráfica).
- Configurações personalizadas de proxy para o MITM Proxy.

### `src/mitm_script.py`

Um script do MITM Proxy para interceptar respostas HTTP, analisar os dados e salvá-los em arquivos JSON. Principais características:

- Filtra requisições para URLs específicas.
- Registra o status HTTP, os cabeçalhos e o corpo da resposta.

## Exemplo de Saída

Os arquivos JSON gerados no diretório `products` terão a seguinte aparência:

```json
{
    "Host": "servicespub.prod.api.aws",
    "Path": "/api/path",
    "URL": "https://servicespub.prod.api.aws/api/path",
    "Status": 200,
    "Headers": {
        "Content-Type": "application/json"
    },
    "Body": {
        "key": "value"
    }
}
```

## Notas

- Certifique-se de que o MITM Proxy está devidamente instalado e acessível no PATH do seu sistema.
- Modifique a função `response` em `src/mitm_script.py` para lidar com formatos adicionais de resposta, se necessário.
