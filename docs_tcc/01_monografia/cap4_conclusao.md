---
fonte: "revisao_tcc/Template_TCC_FEE/Capitulos/Cap_4_ Conclusao.tex"
gerado_em: 2026-09-12
---

Nota: o nome do arquivo tem um espaço antes de "Conclusao" (`Cap_4_ Conclusao.tex`), preservado no `\input` do documento mestre.

## Seção "Considerações Finais"

- Os subsistemas do projeto foram "meticulosamente desenvolvidos e testados, com resultados positivos", cobrindo: modelagem matemática, protótipo, firmware, softwares de interface e gêmeo digital.
- **Sobre a modelagem matemática (contribuição/limitação apontada pelo autor)**: fundamentada nos princípios de Newton, mas o processo "demonstrou que a modelagem de sistemas pode rapidamente se tornar complexa e impraticável"; mesmo com um modelo obtido, a determinação dos coeficientes finais é árdua (requer sensores para medir grandezas físicas). Isso justifica o uso complementar de identificação de sistemas.
- **Sobre o protótipo**: projetado com foco em simplicidade de construção, materiais de baixo custo e componentes eletrônicos amplamente disponíveis — objetivo explícito de ampliar o alcance do projeto (acadêmico e entusiastas).
- **Sobre os testes/validação**: identificação de sistemas e controlador PID em malha fechada foram bem-sucedidos como *validação de infraestrutura*, não como estudo de desempenho aprofundado.
- **Limitação explicitamente reconhecida pelo autor**: "cabe destacar que os testes mencionados anteriormente não foram conduzidos com o intuito primário de obter resultados qualitativos ou quantitativos. Eles foram realizados exclusivamente como uma etapa de validação das funcionalidades desenvolvidas". Ou seja, o próprio autor delimita o escopo dos resultados como prova de conceito/infraestrutura, não como pesquisa de controle rigorosa.
- Conclusão: projeto validado e "pronto para ser implementado em disciplinas associadas a sistemas de controle", com aplicabilidade também em pesquisa acadêmica.

## Principais contribuições (extraídas do texto)

1. Laboratório virtual de baixo custo completo (protótipo + firmware + interface + gêmeo digital) para ensino/pesquisa em sistemas de controle.
2. Infraestrutura de aquisição de dados e ensaio (PRBS, malha aberta/fechada) validada e reutilizável.
3. Pipeline de identificação de sistemas por mínimos quadrados aplicado e validado qualitativamente.
4. Controlador PID em malha fechada funcional integrado ao firmware, com arquitetura que permite trocar controladores facilmente (basta implementar nova biblioteca).

## Trabalhos futuros sugeridos pelo autor

- Estudos de **identificação de sistemas** explorando diferentes métodos (além de mínimos quadrados).
- Desenvolvimento de **controladores** por abordagens clássicas ou com **Inteligência Artificial** — cita especificamente aprendizagem por reforço, deep Q-learning e "outros algoritmos relevantes".
- Expansão do laboratório virtual: novas funcionalidades na interface gráfica e no próprio protótipo físico.
- Elaboração de **documentação abrangente**, a ser disponibilizada online via GitHub (referência ao apêndice do TCC com o link do repositório).
- Criação de **vídeos explicativos** detalhando cada aspecto do projeto.
- Projeto declarado **open source**, aberto a contribuições de pesquisadores, estudantes e entusiastas, com objetivo de "aprimoramento contínuo" e "ampla disseminação do conhecimento".
- Espaço aberto (mencionado nas Considerações Finais) para "futuras pesquisas direcionadas à elaboração de modelos mais precisos e controladores mais robustos".

## Limitações (consolidado)

- Modelagem analítica newtoniana difícil de aplicar por causa de parâmetros físicos de difícil obtenção (momento de inércia, amortecimento viscoso).
- Testes conduzidos como validação de infraestrutura, não como avaliação de desempenho rigorosa (sem métricas quantitativas de erro).
- Modelo de identificação de 2ª ordem não funcionou; foi necessário ir a um modelo de 10ª ordem, validado apenas qualitativamente (visualmente), sem métrica de erro reportada.
- Sintonia do PID feita por tentativa e erro, não por método sistemático.
