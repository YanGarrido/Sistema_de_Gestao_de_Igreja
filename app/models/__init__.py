# __init__.py ou arquivo central onde você configura o banco de dados

from .membros import Membro
from .ministerio import Ministerio
from .membros_ministerio import MembroMinisterio  # Importe a tabela intermediária por último