from src.business_object.attack.abstract_attack import AbstractAttack
class FixedDamagedAttack(AbstractAttack):
    def __init__(self,power, name, description):
        super().__init__(power, name, description)
    def compute_damage(pkm1, pkm2):
        return self._power

        