from opshin.ledger.interval import *


# This should validate if the transaction has a signature from the parameterized beneficiary
# and the deadline has passed.
def validator(
    beneficiary: PubKeyHash, deadline: POSIXTime, redeemer: None, context: ScriptContext
) -> None:
    assert beneficiary in context.tx_info.signatories and contains(
        make_from(deadline), context.tx_info.valid_range
    )
