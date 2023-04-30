from opshin.ledger.interval import *


@dataclass()
class VestingDatum(PlutusData):
    beneficiary1: PubKeyHash
    beneficiary2: PubKeyHash
    deadline: POSIXTime


# This should validate if either beneficiary1 has signed the transaction and the current slot is before or at the
# deadline or if beneficiary2 has signed the transaction and the deadline has passed.
def validator(datum: VestingDatum, redeemer: None, context: ScriptContext) -> None:
    is_signed1 = datum.beneficiary1 in context.tx_info.signatories
    is_signed2 = datum.beneficiary2 in context.tx_info.signatories
    is_before = contains(make_to(datum.deadline), context.tx_info.valid_range)
    is_after = contains(make_from(datum.deadline + 1), context.tx_info.valid_range)
    assert (is_signed1 and is_before) or (is_signed2 and is_after)
