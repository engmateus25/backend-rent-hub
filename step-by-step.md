# 📘 Guia Prático de Desenvolvimento - Equipment Rent API

Este guia descreve, de forma clara e progressiva, os passos necessários para alcançar os seguintes objetivos de aprendizado e implementação no projeto **Equipment Rent**.

---

## ✅ Objetivo 1: Compreender o desenvolvimento básico de uma API com FastAPI

### Etapas:

1. **Criar o projeto base com FastAPI**
   - Estruturar diretório inicial do projeto
   - Criar ambiente virtual e instalar FastAPI e Uvicorn

2. **Configurar o ponto de entrada da aplicação**
   - Criar o arquivo principal (`main.py`) para instanciar a aplicação FastAPI

3. **Definir estrutura de roteamento**
   - Criar diretório de rotas (`/api`)
   - Separar rotas por domínio (ex: `auth.py`, `users.py`, `equipments.py`)

4. **Habilitar documentação automática**
   - Verificar exibição automática via Swagger UI e Redoc no navegador

5. **Testar o servidor localmente**
   - Subir a aplicação com Uvicorn e verificar se responde aos endpoints

---

## ✅ Objetivo 2: Dominar a implementação da modelagem do banco de dados com Tortoise ORM

### Etapas:

1. **Definir os modelos de dados**
   - Criar diretório `models` para armazenar as entidades (User, Equipment, Reservation etc.)

2. **Modelar as tabelas conforme os requisitos**
   - Traduzir os campos e relacionamentos descritos no guia para entidades ORM

3. **Configurar a conexão com o banco**
   - Criar arquivo de configuração com URI de conexão e mapeamento das entidades

4. **Habilitar migrações (opcional)**
   - Integrar Aerich ou outra ferramenta de versionamento de schema

5. **Testar a criação automática das tabelas**
   - Executar o projeto e validar se o banco foi populado com a estrutura esperada

---

## ✅ Objetivo 3: Dominar as queries de banco de dados com uma ORM (Tortoise ORM)

### Etapas:

1. **Definir interfaces para repositórios**
   - Criar diretório `interfaces/repositories`
   - Declarar métodos esperados para manipulação de cada entidade (ex: `get_by_id`, `create`, `update`, `delete`, etc.)

2. **Criar implementações concretas dos repositórios**
   - Criar diretório `repositories` para as implementações das interfaces
   - Garantir que cada classe implementa a respectiva interface

3. **Implementar operações CRUD básicas**
   - Criar, buscar, atualizar e excluir registros para cada entidade

4. **Utilizar filtros e joins**
   - Utilizar recursos como `filter`, `exclude`, `prefetch_related`, entre outros

5. **Integrar com os serviços de negócio**
   - Os serviços devem consumir as interfaces dos repositórios, permitindo fácil substituição ou mock

6. **Validar consistência dos dados**
   - Testar operações com dados reais e validar os resultados retornados

---

## ✅ Objetivo 4: Entender a arquitetura de pastas do projeto

### Etapas:

1. **Separar responsabilidades por domínio**
   - Criar pastas específicas para: `api`, `models`, `schemas`, `services`, `repositories`, `interfaces`, `core`

2. **Definir interfaces para os serviços**
   - Criar diretório `interfaces/services` com definições que descrevam a responsabilidade de cada serviço

3. **Implementar os serviços com base nas interfaces**
   - Criar diretório `services` com as classes que implementam as interfaces previamente definidas
   - Garantir que cada serviço encapsule a lógica de negócio de forma clara e testável

4. **Organizar a estrutura de forma escalável**
   - Aplicar princípios de coesão e baixo acoplamento entre os módulos

5. **Centralizar configurações do sistema**
   - Criar pasta `core` para armazenar configurações (banco, autenticação, variáveis de ambiente, utilitários comuns)

6. **Aplicar padrão de inicialização**
   - O `main.py` deve importar e registrar todas as dependências, rotas, middlewares e configurações

---

## ✅ Objetivo 5: Dominar o fluxo de autenticação com JWT Token

### Etapas:

1. **Definir entidade de autenticação**
   - Criar modelo `UserAuth` com campos como `username`, `password_hash` e vínculo com a entidade `User`

2. **Criar interfaces e serviços de autenticação**
   - Definir interface de autenticação na pasta `interfaces/services`
   - Criar implementação concreta que trate login, registro, validação de senha e geração de token

3. **Gerar e assinar o token JWT**
   - Criar utilitário para gerar tokens JWT com tempo de expiração e dados do usuário

4. **Implementar verificação de token**
   - Criar dependência para extrair e validar o token nas rotas privadas

5. **Proteger rotas com autenticação**
   - Aplicar `Depends` nas rotas que exigem usuário autenticado

6. **Aplicar controle de acesso (roles ou permissões)**
   - (Opcional) Definir tipos de usuário e permissões específicas por recurso

---

📌 Ao seguir essas instruções, você terá uma API funcional, segura, desacoplada e bem estruturada, seguindo boas práticas de arquitetura orientada a interfaces no projeto Equipment Rent.
