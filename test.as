.PROGRAM testsakamoto
    WHILE abc!=100 do
        PROMPT"nyuryoku:",abc
            IF abc==4 THEN
                HOME
                 JMOVE pos1
                 JMOVE pos2
                 JMOVE pos3
                 JMOVE pos2
                 JMOVE pos1
                 JMOVE pos4
                 JMOVE pos1
                 HOME
            ELSEIF abc<4 THEN
                JMOVE pos2
                HOME
            END
    END
.EMD

位置変数
pos1    140.0   270.0   270.0   35.0    0.0 0.0
pos2    140.0   550.0   270.0   35.0    0.0 0.0
pos3    140.0   550.0   25.0   35.0    0.0 0.0
pos4    140.0   270.0   35.0   35.0    0.0 0.0
