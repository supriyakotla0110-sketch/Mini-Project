def get_resolution(category):

    resolutions = {

        "Credit card or prepaid card": """
1. Check recent transactions.
2. Contact your card issuer.
3. Raise a dispute for unauthorized charges.
4. Request transaction investigation.
""",

        "Mortgage": """
1. Review mortgage documents.
2. Contact your lender.
3. Request a written explanation.
""",

        "Debt collection": """
1. Verify the debt.
2. Request written proof.
3. Report harassment if applicable.
""",

        "Student loan": """
1. Check repayment details.
2. Contact loan servicer.
3. Explore deferment options.
""",

        "Checking or savings account": """
1. Review account transactions.
2. Contact the bank.
3. Report unauthorized activity.
"""
    }

    return resolutions.get(
        category,
        "Please contact customer support for assistance."
    )