# Documentação de Requisitos para MVP - Sistema de Geração de Artefatos para QAs

## 1. Visão Geral do Projeto

O sistema tem como objetivo permitir que **QAs (Quality Analysts)** possam gerar **artefatos de teste** e **relatórios** de maneira simples e eficiente. O sistema vai utilizar uma **API de Modelos de Linguagem (LLM)** para gerar automaticamente os artefatos com base em dados fornecidos pelos usuários.

Este **MVP** será uma versão simplificada do sistema, com funcionalidades essenciais para a geração de artefatos e com um foco em uma interface básica, visando entregar valor rapidamente sem sobrecarga de funcionalidades avançadas.

---

## 2. Requisitos Funcionais

### 2.1 Funcionalidades Essenciais

#### 1. **Login e Registro**
- **Objetivo**: Permitir que os usuários se cadastrem e façam login no sistema.
- **Requisitos**:
  - O sistema deve permitir que novos usuários se registrem com um nome de usuário e senha.
  - O sistema deve permitir que os usuários já registrados façam login utilizando o nome de usuário e senha.
  - O sistema deve **armazenar senhas de forma segura** (pode ser utilizando hash, como bcrypt).
  - Não será necessário adicionar funcionalidades de recuperação de senha nesse MVP.

#### 2. **Geração de Artefatos**
- **Objetivo**: Gerar automaticamente artefatos (como casos de teste e relatórios) com base em inputs do usuário.
- **Requisitos**:
  - O usuário deve ser capaz de inserir **descrições simples** de bugs, requisitos ou casos de teste.
  - A descrição inserida será enviada para uma API de LLM (como **OpenAI GPT-3** ou similar) para gerar o artefato correspondente.
  - O sistema deve **exibir** os artefatos gerados de maneira simples, no formato de texto.
  - Os artefatos gerados serão **temporariamente armazenados na sessão do usuário**, sem persistência em banco de dados (sem armazenamento a longo prazo no MVP).

#### 3. **Visualização e Download de Artefatos**
- **Objetivo**: Permitir ao usuário visualizar e **baixar** os artefatos gerados.
- **Requisitos**:
  - O sistema deve exibir os artefatos gerados de forma clara e legível para o usuário.
  - O usuário deve poder **baixar o artefato em formato de texto** (arquivo `.txt`).
  
#### 4. **Interface Simples de Usuário**
- **Objetivo**: Criar uma interface gráfica simples para interação.
- **Requisitos**:
  - A interface deve ter um campo para inserir a descrição do bug/requisito.
  - O usuário deve clicar em um botão para **gerar o artefato** a partir da descrição.
  - Após a geração, o artefato deve ser exibido na tela e ser possível de **baixar**.
  - A interface será **simples** e com o mínimo de design (pode ser uma página única).

---

## 3. Requisitos Não Funcionais

### 3.1 Desempenho
- **Tempo de Resposta**: O sistema deve ser capaz de gerar e exibir os artefatos em até **5 segundos** após o envio da descrição para a API de LLM.
- **Simples e Eficiente**: Como é um MVP, não é necessário se preocupar com otimizações de performance em larga escala. O objetivo é garantir que as operações principais sejam feitas de maneira eficiente.

### 3.2 Escalabilidade (Mínima)
- **Escalabilidade Inicial**: O sistema pode ser testado em um ambiente simples, sem a necessidade de escalabilidade no início. A aplicação deve funcionar bem com **poucos usuários simultâneos**.

### 3.3 Usabilidade
- **Interface Simples e Intuitiva**: O sistema deve ser fácil de usar, com instruções claras para o usuário. Um design minimalista é preferível, já que a complexidade do MVP deve ser baixa.
- **Experiência do Usuário**: Deve ser possível para o usuário completar a tarefa de geração de artefatos sem dificuldades (entrada de dados e download do arquivo gerado).

### 3.4 Segurança
- **Autenticação Básica**: Embora o sistema tenha um sistema de login e senha, **não será necessário implementar funcionalidades avançadas de segurança** neste MVP, como autenticação multifatorial.
- **Armazenamento de Senha Seguro**: As senhas devem ser armazenadas de forma segura no banco de dados, utilizando técnicas básicas de hashing, como bcrypt.

### 3.5 Armazenamento de Dados
- **Sem Persistência Complexa**: No MVP, os artefatos gerados serão armazenados apenas temporariamente na sessão do usuário e não será necessário armazená-los em um banco de dados persistente. 
- **Banco de Dados**: Não será necessário implementar um banco de dados relacional ou NoSQL neste estágio inicial.

### 3.6 Contêineres e Docker
- **Containerização Simples**: O sistema será **containerizado usando Docker** para facilitar a instalação e execução em qualquer ambiente. A configuração será simplificada, sem a necessidade de orquestração complexa de containers (como Docker Compose).

---

## 4. Cronograma de Desenvolvimento

O cronograma está estruturado para ser simples e realista para um desenvolvedor iniciante. O foco será na entrega rápida do MVP, com as funcionalidades essenciais funcionando.

### Fase 1: Planejamento e Preparação (1 Semana)
- Definição de tecnologias: Escolher as tecnologias para o frontend (React) e backend (FastAPI ou Python).
- Preparação do ambiente de desenvolvimento local (Docker e dependências básicas).

### Fase 2: Desenvolvimento do Backend (1 Semana)
- Implementação do microserviço de **Autenticação** (registro e login de usuário).
- Criação do microserviço para **geração de artefatos** com a API de LLM.
  
### Fase 3: Desenvolvimento do Frontend (1 Semana)
- Criação da interface simples de usuário em **React**.
- Conectar o frontend com o backend para permitir a geração de artefatos e download.

### Fase 4: Testes e Ajustes (1 Semana)
- Testes unitários para o backend (validação das APIs).
- Testes de usabilidade da interface.
- Ajustes de UX (experiência do usuário).

### Fase 5: Documentação e Deploy (1 Semana)
- Documentação simples de como usar o sistema e executar o backend/frontend localmente.
- Deploy no ambiente de desenvolvimento (pode ser local ou em uma plataforma simples como **Heroku** ou **Railway**).

---

## 5. Conclusão

Este **MVP** visa entregar um sistema básico, mas funcional, que permitirá a geração de artefatos de teste para QAs, com foco na simplicidade e usabilidade. O desenvolvimento será feito de maneira incremental, com funcionalidades essenciais entregues primeiro e mais complexidade adicionada em fases posteriores.

Se você tiver alguma dúvida ou precisar de mais detalhes sobre qualquer parte do desenvolvimento, estou à disposição para ajudar!
