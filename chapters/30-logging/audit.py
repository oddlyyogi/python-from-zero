import logging

log = logging.getLogger("ledger")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    filename="ledger.log",
    filemode="w",
)

log.debug("opening ledger file")
log.info("loaded 3 transactions")
log.warning("rent amount is unusually large")
log.error("could not parse line 7")
log.critical("ledger file is missing")

try:
    float("abc")
except ValueError:
    log.exception("could not parse amount")
log.info("added %s for %.2f", "coffee", 4.5)
