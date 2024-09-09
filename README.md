# midi_ear_training
Joguinho para treinar o ouvido para identificar progressões de acordes e intervalos entre notas.
Até o momento apenas a parte de progressões está desenvolvida.

Modo de uso:
1) Execute o script `create_chod_progressions.py` para popular o disco com os arquivos midi correspondente às progressos
2) Uma vez que os midis já tenham sido criados basta executar o script `chord_progression_game.py` para jogar.

*OBS* : As entradas válidas são sequências de algorismos romanos de 1 a 7 (I a VII) separados por espaço onde algorismos maiúsculos denotam acordes maiores e minúsculos denotam acordes menores.
Exemplo de entradas válidas: I vi V iv | i III v i | I IV V
Exemplo de entradas inválidas: I, vi, V, iv | i VIII v i | I iV V
Ao entrar uma sequência válida o jogo irá reproduzí-la para que o usuário possa comprar com o som da sequência alvo.
