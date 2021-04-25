class InvalidRuleNameError(Exception):
    """Raised when the rule doesn't match any RequestHandler function."""

    def __init__(self, rule, message="Used invalid rule name: "):
        self.rule = str(rule)
        self.message = message + self.rule
        super().__init__(self.message)
