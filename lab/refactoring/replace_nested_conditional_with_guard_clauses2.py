# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
<<<<<<< HEAD:lab/refactoring/replace_nested_conditional_with_gaurd_clauses2.py
# Replace nested conditional with gaurd clases.

=======
# Replace nested conditional with guard clases.
>>>>>>> 67a0de20719a1f2b5386fb1cb1ad7ffa716ed466:lab/refactoring/replace_nested_conditional_with_guard_clauses2.py
ADJ_FACTOR = 0.7
def get_adjusted_capital(capital, rate, duration, income):
    result = 0
    if (capital < 0):
        return 0
    if (rate > 0 and duration > 0):
        result = (income / duration) * ADJ_FACTOR
    
    return result

adjusted_capital = get_adjusted_capital(50000, 4,10, 10000)
print(adjusted_capital)