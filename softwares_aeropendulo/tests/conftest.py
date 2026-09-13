import sys
from pathlib import Path

PACOTE = Path(__file__).resolve().parents[1]
RAIZ = PACOTE.parent
sys.path.insert(0, str(PACOTE))
