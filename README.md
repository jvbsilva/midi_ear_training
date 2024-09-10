# midi_ear_training
Joguinho para treinar o ouvido a identificar progressões de acordes e intervalos entre notas.
Até o momento apenas a parte de progressões está desenvolvida.

Modo de uso:
- Basta executar o script `chord_progression_game.py` para jogar.

Regras:
- As entradas válidas são sequências de algarismos romanos de 1 a 7 (I a VII) separados por espaço onde algarismos maiúsculos denotam acordes maiores e minúsculos denotam acordes menores.

- Exemplo de entradas válidas: I vi V iv | i III v i | I IV V

- Exemplo de entradas inválidas: I, vi, V, iv | i VIII v i | I iV V

- Ao entrar uma sequência válida o jogo irá reproduzí-la para que o usuário possa comparar com o som da sequência alvo.

**OBS 1:** As progressões que fazem parte do jogo estão armazenadas na lista `PROGRESSIONS` no arquivo `create_chord_progressions.py`. Caso queria adicionar ou excluir progressões basta alterar essa lista.

**OBS 2:** Caso queira gerar todas as progressões e armanezar em disco para inspeção basta executar o script `create_chord_progressions.py`


Próximos passos:
- Armazenar o número de tentativas que o usuário levou até acertar em um banco de dados para que ele possa acompanhar seu progresso.
