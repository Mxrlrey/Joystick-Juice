# Joystick-Juice  
### Sistema desenvolvido para avaliações de games jogados

---

## 📋 Visão Geral

Este repositório contém o **Joystick-Juice**, uma plataforma voltada exclusivamente para avaliações de jogos. Aqui, você encontrará:

- **Reviews detalhadas**: análises de cada jogo, com notas para gráficos, jogabilidade, história e música.  
- **Listas personalizáveis**: crie e compartilhe suas próprias listas, como "Jogos Favoritos", "Aventura Épica" ou "Indie Imperdível".  
- **Sistema de notas e rankings**: descubra os jogos mais bem avaliados pela comunidade.  
- **Perfis de usuários**: acompanhe o histórico de jogos jogados, suas avaliações e conquistas.  

---

## 📌 Índice

1. [Funcionalidades](#funcionalidades)  
2. [Requisitos Funcionais](#requisitos-funcionais)  
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)  
4. [Como Rodar o Projeto](#como-rodar-o-projeto)  
5. [Repositório Online](#repositório-online)  
6. [Autores](#autores)  

---

## 🎮 Funcionalidades

- **Cadastro e Autenticação**  
  - Registro de novos usuários e login seguro.  
- **Catálogo de Jogos**  
  - Navegue por uma vasta lista de títulos, com filtros por gênero, plataforma e data de lançamento.  
- **Reviews e Avaliações**  
  - Escreva comentários detalhados e atribua notas individuais (gráficos, gameplay, narrativa, som).  
- **Listas Personalizadas**  
  - Crie, edite e compartilhe listas temáticas de jogos.  
- **Ranking da Comunidade**  
  - Visualize os jogos mais avaliados e populares.  
- **Perfis de Usuário**  
  - Acompanhe seu histórico de avaliações, listas e conquistas.  
- **Busca Avançada**  
  - Pesquise jogos por título, desenvolvedor ou estilo.  

---

## 📋 Requisitos Funcionais

| ID     | Descrição                                                                                                                       | Prioridade | Módulo             |
|--------|---------------------------------------------------------------------------------------------------------------------------------|------------|--------------------|
| RF001  | O sistema deve permitir cadastro.                                                                                              | Alta       | Autenticação       |
| RF002  | O sistema deve permitir login.                                                                                                 | Alta       | Autenticação       |
| RF003  | O sistema deve permitir recuperar senha.                                                                                       | Alta       | Autenticação       |
| RF004  | O sistema deve ter a possibilidade de logout.                                                                                  | Alta       | Autenticação       |
| RF005  | O sistema deve ter uma página inicial mostrando os jogos por nome, gênero, popularidade e nota.                                 | Alta       | Catálogo de Jogos  |
| RF006  | O sistema deve permitir ao usuário favoritar jogos.                                                                            | Média      | Perfil / Social    |
| RF007  | O sistema deve permitir ao usuário seguir outros usuários e ser seguido.                                                       | Média      | Perfil / Social    |
| RF008  | O sistema deve permitir a criação de reviews para jogos, visíveis publicamente.                                                | Alta       | Reviews            |
| RF009  | O sistema deve ter uma sidebar com informações como: perfil, configurações, etc.                                               | Média      | Interface Usuário  |
| RF010  | O sistema deve permitir ao usuário adicionar um novo jogo ao seu catálogo pessoal com uma nota de avaliação, status (playing, played, on hold, dropped, plan to play) e comentários opcionais. | Alta       | Listas de Jogos    |
| RF011  | Na aba de perfil, o sistema deve possibilitar ao usuário editar suas informações, ver seus seguindo e seguidores, mostrar seus jogos favoritos, ver sua lista de jogos, visualizar suas últimas atividades e acessar estatísticas como número de jogos finalizados, tempo estimado jogado e média de nota atribuída. | Alta       | Perfil / Estatísticas |
| RF012  | O sistema deve permitir filtrar jogos por status na página do usuário.                                                         | Média      | Listas de Jogos    |
| RF013  | O sistema deve enviar notificações ao usuário quando for seguido, receber um comentário ou quando um jogo for lançado/atualizado.| Média      | Notificações       |
| RF014  | Na lista de jogos do usuário, deve ser possível visualizar todos os jogos que ele adicionou, organizados por status; adicionar, editar ou remover comentários; e adicionar ou remover jogos da lista. | Alta       | Listas de Jogos    |
| RF015  | Ao acessar a página de um jogo específico, deve ser possível ver sua sinopse, nota, popularidade, desenvolvedora, criadores e as reviews feitas pelos usuários. | Alta       | Catálogo de Jogos  |
| RF016  | O sistema deve permitir ao usuário avaliar e comentar nas reviews de outros usuários (ex: curtir, responder, denunciar).        | Média      | Reviews / Social   |
| RF017  | O sistema deve permitir ver rankings dos jogos mais populares, mais bem avaliados ou mais comentados.                          | Média      | Rankings           |
| RF018  | O sistema deve ter um mecanismo de busca avançada com múltiplos filtros combinados (gênero + plataforma + nota mínima, etc).   | Alta       | Busca              |

---

## 📋 Requisitos Não Funcionais

| ID     | Descrição                                                                                                                   | Prioridade | Módulo               |
|--------|-----------------------------------------------------------------------------------------------------------------------------|------------|----------------------|
| RNF001 | O sistema deve utilizar protocolo HTTPS para garantir segurança na transmissão de dados.                                   | Alta       | Segurança            |
| RNF002 | Senhas dos usuários devem ser armazenadas com algoritmos de hash seguros (ex: bcrypt).                                      | Alta       | Segurança            |
| RNF003 | O tempo de resposta para carregamento de páginas deve ser inferior a 2 segundos.                                            | Alta       | Desempenho           |
| RNF004 | O sistema deve ser responsivo e adaptável a dispositivos móveis e desktops.                                        | Alta       | Interface Usuário    |
| RNF005 | O site deve estar disponível 99,5% do tempo.                                                                                 | Alta       | Confiabilidade       |
| RNF006 | O sistema deve ser compatível com os navegadores modernos: Chrome, Firefox, Safari e Edge.                                 | Média      | Compatibilidade      |
| RNF007 | O sistema deve seguir as diretrizes de acessibilidade WCAG 2.1.                                                             | Média      | Acessibilidade       |
| RNF008 | A arquitetura do sistema deve permitir fácil escalabilidade para suportar aumento de usuários simultâneos.                 | Média      | Escalabilidade       |
| RNF009 | O código-fonte deve seguir boas práticas de desenvolvimento (ex: padrão de projeto, separação de camadas, documentação).    | Alta       | Manutenibilidade     |
| RNF010 | Deve haver backup automático do banco de dados ao menos uma vez por dia.                                                    | Alta       | Confiabilidade       |
| RNF011 | O sistema deve implementar logs de erro e logs administrativos com data, hora e autor da ação.                             | Alta       | Auditabilidade       |
| RNF012 | A recuperação de falhas deve apresentar mensagens de erro amigáveis ao usuário e registrar os erros para análise posterior. | Média      | Confiabilidade       |
| RNF013 | O sistema deve suportar até 1000 usuários simultâneos sem degradação perceptível de performance.                           | Média      | Desempenho           |
| RNF014 | Deve haver testes automatizados para funcionalidades críticas do sistema.                                                   | Média      | Qualidade / Testes   |
| RNF015 | O sistema deve permitir rastrear ações administrativas, como exclusão de reviews ou bloqueio de contas.                    | Alta       | Segurança / Auditoria|

---

## 🛠️ Tecnologias Utilizadas

- **MySQL**: banco de dados relacional para armazenamento de usuários, jogos, reviews e listas.  
- **Python**: lógica de backend, APIs e scripts de análise.  
- **Visual Studio Code**: IDE principal para desenvolvimento.  
- **Django**: framework web para desenvolvimento backend.  

---

## 🌐 Repositório Online

Acesse o código completo em:

🔗 [GitHub - Joystick Juice](https://github.com/Mxrlrey/Joystick-Juice)

---

## 👨‍💻 Autores

Desenvolvido por:  
- Djavan Teixeira Lopes  
- Gabriel Rocha Gomes  
- Marley Teixeira Meira  

---
