import math

class MathService:
    """Service to safely evaluate math expressions."""

    def __init__(self):
        # Create a dictionary with allowed math functions
        self.safe_dict = {
            k: getattr(math, k) for k in dir(math) if not k.startswith("__")
        }
        # Also add constants and basic functions
        self.safe_dict.update({
            "abs": abs,
            "round": round,
            "min": min,
            "max": max
        })

    def calculate(self, expression: str):
        """
        Safely evaluate a math expression.

        Args:
            expression (str): The math expression to evaluate, e.g. "2+2*3".
        Returns:
            str: The result as a string, or error message.
        """
        try:
            result = eval(expression, {"__builtins__": {}}, self.safe_dict)
            return str(result)
        except Exception as e:
            print(f"Math evaluation error: {e}")
            return f"Error: Could not evaluate '{expression}'. Please check your input."
