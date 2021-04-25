from exceptions import InvalidRuleNameError


class RuleDataHandler:
    """Provide collection of functions to handle list of numbers."""

    functions = {
        'a': lambda x: x ** 2,     # fun_a
        'b': lambda x: 2 * x + 1,  # fun_b
        'c': lambda x: x - 1,      # fun_c
        'd': lambda x: x / 10,     # fun_d
        'e': lambda x: x + 10,     # fun_e
        'f': lambda x: x / 2,      # fun_f
    }

    def __init__(self, request_data):
        self.data = request_data["data"]
        self.rules = request_data["rule"].strip()

    def apply(self):
        """
        Applying each function (rule) to all numbers in the list.
        Example:
            data: [1, 2, 3, 4, 5, 6]
            handling: [fun_a([1, 2, 3, 4, 5, 6]), ... fun_f([1, 2, 3, 4, 5, 6])]
        """
        result = []
        for function in self._get_functions_by_rules():
            result += [function(n) for n in self.data]
        
        return result

    def apply_by_pairs(self):
        """
        Apply rules (functions) to ach numbers in the list by pairs.
        Example:
            data: [1, 2, 3, 4, 5, 6]
            handling: [fun_a(1), fun_b(2), ... fun_f(6)]
        """
        result = []
        for function, num in zip(self._get_functions_by_rules(), self.data):
            result.append(function(num))
        
        return result

    def _get_functions_by_rules(self):
        try:
            return [self.functions[rule] for rule in self.rules.split()]
        except KeyError as exc:
            raise InvalidRuleNameError(exc)
