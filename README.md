# 🎵 Otimização de Progressões de Acordes Musicais com Teoria dos Grafos

![Status](https://img.shields.io/badge/Status-Finalizado-success)
![Linguagem](https://img.shields.io/badge/Linguagem-Python-blue)
![Matemática](https://img.shields.io/badge/Matemática-Teoria_dos_Grafos-orange)

Este projeto une fundamentos de Ciência da Computação e Teoria Musical para resolver um problema clássico de harmonia: a otimização do deslocamento físico das mãos ao tocar um instrumento. Desenvolvido originalmente como uma pesquisa de matemática discreta no Instituto Federal do Espírito Santo (IFES) - Campus Serra, o estudo modela acordes como grafos e aplica o **Algoritmo de Dijkstra** para encontrar o caminho de menor custo (em semitons) em uma progressão harmônica.

## O Problema: Voice Leading e Esforço Físico
Ao tocar uma progressão de acordes (como Dó Maior -> Sol Maior -> Ré Maior), o uso exclusivo de acordes no estado fundamental exige saltos longos e pouco naturais no instrumento. Músicos utilizam **inversões de acordes** para encurtar essa distância (técnica conhecida como *voice leading*). 

No entanto, em progressões longas, calcular mentalmente a sequência exata de inversões que gera o menor deslocamento total é um desafio. 

## Modelagem Matemática
Para solucionar isso computacionalmente, o cenário foi modelado matematicamente da seguinte forma:
* **Nós (Vértices):** Representam os acordes e suas possíveis inversões (Estado fundamental, 1ª inversão, 2ª inversão).
* **Arestas:** Representam as transições possíveis entre um acorde e o próximo na progressão.
* **Pesos:** Representam o custo físico, medido em **semitons** percorridos pelo baixo de uma inversão até a subsequente.

O **Algoritmo de Dijkstra** foi implementado para varrer a Matriz de Adjacências e determinar o caminho mínimo global, garantindo a sucessão de acordes mais suave possível.

## Resultados
A aplicação do algoritmo comprovou uma otimização drástica na progressão teste (`C -> G -> D`). 
O custo de deslocamento, que originalmente era de **14 semitons** utilizando apenas acordes no estado fundamental, foi reduzido para apenas **2 semitons** utilizando o caminho ótimo de inversões calculado pelo algoritmo.

## 📂 Estrutura do Repositório
* `docs/`: Contém o artigo original completo em PDF detalhando o referencial teórico, as tabelas de semitons e o teste de mesa do algoritmo.
* `src/`: (Futuro) Conterá a implementação do algoritmo em Python.

## 📄 Leia o Artigo Completo
A fundamentação teórica completa, a matriz de adjacências e a execução passo a passo do algoritmo estão documentadas no artigo.

👉 **[Clique aqui para acessar o PDF do artigo completo](./docs/Acordes_MD_IlannaCardoso.pdf)**

---
*Projeto desenvolvido por Ilanna dos Reis Cardoso.*
