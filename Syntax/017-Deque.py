# Deque boyutu önceden belirtilir.

#import edilmesi gerekir.
from collections import deque

# Maksimum uzunluk belirtilir.
# 3 den fazla veri eklendiğinde baştaki veri silinir.
dq = deque(maxlen = 3)

# Listenin sonuna ekleme işlemi
dq.append(1)

# Listenin başına ekleme işlemi
dq.appendleft(3)

# Listeyi temizleme
dq.clear()

#
